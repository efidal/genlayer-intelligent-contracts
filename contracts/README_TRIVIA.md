# TriviaQuiz — AI-Powered Trivia Game on GenLayer

> GenLayer Mission: Mini-games for GenLayer's Community | Testnet Bradbury 2026

## What is TriviaQuiz?

TriviaQuiz is a fully decentralized trivia game built as a GenLayer Intelligent Contract.

The AI generates questions on any topic, players submit answers, and LLM consensus acts as a fair judge — accepting synonyms, minor typos, and partial answers. No centralized question bank. No hardcoded answers. Pure AI on-chain.

**This would be impossible on any other blockchain.**

## How It Works

```
Player picks a category:  "Bitcoin"
                ↓
GenLayer AI generates on-chain:
  Q: "In what year was Bitcoin created?"
                ↓
Player submits answer: "2009"
                ↓
AI Consensus judges:
  [GPT-4]  → CORRECT
  [Claude] → CORRECT
  [Llama]  → CORRECT
                ↓
      ✅ CORRECT! Score: +1 point (stored on-chain)
```

## Key Functions

| Function | Description |
|---|---|
| `generate_question(category)` | AI generates a trivia question on any topic |
| `submit_answer(question_id, answer)` | Submit your answer |
| `check_answer(question_id, player)` | AI judges if the answer is correct |
| `quick_play(category, answer)` | Generate + answer in one transaction |
| `get_score(player_address)` | Get a player's total score |
| `get_question(question_id)` | View a question |

## Example Usage

```python
# Quick demo — one transaction
contract.quick_play(
    category="Space",
    answer="Neil Armstrong"
)
# → Q: "Who was the first human to walk on the Moon?"
# → Your answer: "Neil Armstrong" | CORRECT! Score: 1 points

# Step by step
qid = contract.generate_question("Football")
# → Question #3: "Which country won the 2022 FIFA World Cup?"

contract.submit_answer(3, "Argentina")
contract.check_answer(3, my_address)
# → CORRECT! Score: 2 points
```

## Why GenLayer Makes This Unique

| Feature | Traditional Blockchain | GenLayer |
|---|---|---|
| Question generation | ❌ Hardcoded / centralized | ✅ AI generates on-chain |
| Answer judging | ❌ Exact string match only | ✅ LLM understands meaning |
| Fair consensus | ❌ Single point of truth | ✅ Multiple validators agree |
| Any topic | ❌ Limited predefined set | ✅ Infinite categories |

## Try It Yourself

1. Open [GenLayer Studio](https://studio.genlayer.com)
2. Deploy `trivia_quiz.py`
3. Call `quick_play("Bitcoin", "Satoshi Nakamoto")`
4. Watch the AI generate a question and judge your answer in real time

## Deployed On

- Network: GenLayer Testnet Bradbury
- Contract: *(address after deploy)*
