# trivia_quiz.py
# GenLayer Intelligent Contract — AI Trivia Quiz Game
# Mission: Mini-games for GenLayer's Community
#
# How it works:
# 1. Anyone generates a trivia question (AI creates it on-chain)
# 2. Players submit their answers
# 3. AI Consensus judges if the answer is correct
# 4. Scores stored permanently on-chain
#
# Showcases GenLayer's unique powers:
# → LLM generates content on-chain (no centralized question bank)
# → LLM consensus judges subjective answers (no rigid string matching)

from genlayer import *


@gl.contract
class TriviaQuiz(gl.Contract):
    """
    AI-powered Trivia Quiz Game on GenLayer.

    Players can generate questions, submit answers, and earn on-chain scores.
    The AI acts as both question creator and judge — fully decentralized.
    """

    owner: str
    question_count: u256
    questions: TreeMap[u256, str]       # question_id → question text
    answers: TreeMap[u256, str]         # question_id → correct answer
    categories: TreeMap[u256, str]      # question_id → category
    difficulties: TreeMap[u256, str]    # question_id → EASY / MEDIUM / HARD
    scores: TreeMap[str, u256]          # player address → total correct answers
    player_answers: TreeMap[str, str]   # "qid:address" → submitted answer
    answered: TreeMap[str, bool]        # "qid:address" → has answered

    def __init__(self) -> None:
        self.owner = gl.message.sender_address
        self.question_count = u256(0)

    # ─── READ FUNCTIONS ────────────────────────────────────────────────────────

    @gl.public.view
    def get_question(self, question_id: u256) -> dict:
        """Get a question without revealing the answer."""
        return {
            "id": int(question_id),
            "question": self.questions[question_id] if question_id in self.questions else "",
            "category": self.categories[question_id] if question_id in self.categories else "",
            "difficulty": self.difficulties[question_id] if question_id in self.difficulties else "",
        }

    @gl.public.view
    def get_score(self, player_address: str) -> u256:
        """Get a player's total score."""
        if player_address not in self.scores:
            return u256(0)
        return self.scores[player_address]

    @gl.public.view
    def get_total_questions(self) -> u256:
        """Get total number of questions generated."""
        return self.question_count

    @gl.public.view
    def has_answered(self, question_id: u256, player_address: str) -> bool:
        """Check if a player already answered a question."""
        key = f"{int(question_id)}:{player_address}"
        return self.answered[key] if key in self.answered else False

    # ─── WRITE FUNCTIONS ───────────────────────────────────────────────────────

    @gl.public.write
    def generate_question(self, category: str) -> u256:
        """
        Generate a new trivia question using LLM consensus.

        Args:
            category: Topic for the question (e.g. "Science", "History", "Crypto")

        Returns:
            question_id: ID of the newly created question
        """
        assert len(category) >= 3, "Category must be at least 3 characters"
        assert len(category) <= 50, "Category too long"

        prompt = f"""You are a trivia question generator. Create one trivia question about: {category}

Respond in this EXACT format (no extra text):
QUESTION: [A clear, specific trivia question]
ANSWER: [The correct answer, 1-5 words max]
DIFFICULTY: [EASY or MEDIUM or HARD]

Rules:
- Question must be factually verifiable
- Answer must be short and unambiguous
- Do not include the answer in the question
"""

        result = gl.eq_principle_prompt_comparative(
            prompt,
            principle="The trivia generator should produce a factually correct question with an unambiguous answer for the given category."
        )

        question_text = ""
        answer_text = ""
        difficulty = "MEDIUM"

        for line in result.split('\n'):
            line = line.strip()
            if line.startswith('QUESTION:'):
                question_text = line.replace('QUESTION:', '').strip()
            elif line.startswith('ANSWER:'):
                answer_text = line.replace('ANSWER:', '').strip()
            elif line.startswith('DIFFICULTY:'):
                difficulty = line.replace('DIFFICULTY:', '').strip().upper()
                if difficulty not in ["EASY", "MEDIUM", "HARD"]:
                    difficulty = "MEDIUM"

        assert len(question_text) > 5, "Failed to generate a valid question"
        assert len(answer_text) > 0, "Failed to generate a valid answer"

        question_id = self.question_count
        self.questions[question_id] = question_text
        self.answers[question_id] = answer_text
        self.categories[question_id] = category
        self.difficulties[question_id] = difficulty
        self.question_count = u256(int(self.question_count) + 1)

        return question_id

    @gl.public.write
    def submit_answer(self, question_id: u256, answer: str) -> str:
        """
        Submit an answer to a trivia question.

        Args:
            question_id: ID of the question to answer
            answer: Player's answer

        Returns:
            Confirmation message
        """
        assert question_id in self.questions, "Question does not exist"
        assert len(answer) >= 1, "Answer cannot be empty"
        assert len(answer) <= 200, "Answer too long"

        player = gl.message.sender_address
        key = f"{int(question_id)}:{player}"

        assert not (key in self.answered and self.answered[key]), "You already answered this question"

        self.player_answers[key] = answer
        self.answered[key] = True

        return f"Answer submitted for question #{int(question_id)}. Call check_answer to see if you're correct!"

    @gl.public.write
    def check_answer(self, question_id: u256, player_address: str) -> str:
        """
        Check if a player's answer is correct using AI consensus.

        The LLM acts as a fair judge — accepts synonyms, minor typos,
        and partial answers that capture the correct meaning.

        Args:
            question_id: ID of the question
            player_address: Address of the player to check

        Returns:
            Verdict with updated score
        """
        assert question_id in self.questions, "Question does not exist"

        key = f"{int(question_id)}:{player_address}"
        assert key in self.player_answers, "No answer found for this player"

        question = self.questions[question_id]
        correct_answer = self.answers[question_id]
        player_answer = self.player_answers[key]

        prompt = f"""You are a fair trivia judge. Decide if the player's answer is correct.

QUESTION: {question}
CORRECT ANSWER: {correct_answer}
PLAYER'S ANSWER: {player_answer}

Judging rules:
- Accept minor spelling mistakes
- Accept synonyms with the same meaning
- Accept partial answers that contain the key information
- Be case-insensitive
- Do NOT accept completely wrong answers

Respond in this EXACT format:
RESULT: [CORRECT or INCORRECT]
REASON: [One short sentence]
"""

        result = gl.eq_principle_prompt_comparative(
            prompt,
            principle="The trivia judge should consistently reach the same verdict for the same question, correct answer, and player answer."
        )

        is_correct = "RESULT: CORRECT" in result.upper()

        if is_correct:
            current = int(self.scores[player_address]) if player_address in self.scores else 0
            self.scores[player_address] = u256(current + 1)
            return f"CORRECT! Your score: {current + 1} points"
        else:
            current = int(self.scores[player_address]) if player_address in self.scores else 0
            return f"INCORRECT. The correct answer was: {correct_answer}. Your score: {current} points"

    @gl.public.write
    def quick_play(self, category: str, answer: str) -> str:
        """
        One-step: generate a question AND submit your answer in one transaction.
        Useful for quick demo in GenLayer Studio.

        Args:
            category: Topic (e.g. "Space", "Football", "Bitcoin")
            answer: Your answer to the generated question

        Returns:
            Question text + verdict
        """
        question_id = self.generate_question(category)
        question_text = self.questions[question_id]
        self.submit_answer(question_id, answer)
        verdict = self.check_answer(question_id, gl.message.sender_address)
        return f'Q: "{question_text}" | Your answer: "{answer}" | {verdict}'
