# ai_vote.py
# GenLayer Intelligent Contract – AI-Powered Voting System
# Testnet: Bradbury
#
# A voting contract where the final result is validated by LLM consensus.
# The AI checks if votes are legitimate and resolves disputes automatically.

from genlayer import *


@gl.contract
class AIVoteContract:
    """
    Voting contract with AI-based validation and dispute resolution.
    Validators use LLM consensus to verify vote legitimacy.
    """

    owner: str
    proposal: str
    votes_yes: u256
    votes_no: u256
    voters: TreeMap[str, bool]
    is_active: bool

    def __init__(self, proposal: str) -> None:
        self.owner = contract_runner.from_account
        self.proposal = proposal
        self.votes_yes = 0
        self.votes_no = 0
        self.is_active = True

    @gl.public.view
    def get_proposal(self) -> str:
        return self.proposal

    @gl.public.view
    def get_results(self) -> dict:
        return {
            "proposal": self.proposal,
            "yes": int(self.votes_yes),
            "no": int(self.votes_no),
            "total": int(self.votes_yes + self.votes_no),
            "active": self.is_active,
        }

    @gl.public.view
    def has_voted(self, address: str) -> bool:
        return address in self.voters

    @gl.public.write
    def cast_vote(self, vote: bool, reasoning: str) -> str:
        """
        Cast a vote with optional reasoning. LLM validates the reasoning is coherent.

        Args:
            vote: True = Yes, False = No
            reasoning: Why the voter is voting this way

        Returns:
            Confirmation message
        """
        assert self.is_active, "Voting is closed"
        voter = contract_runner.from_account
        assert voter not in self.voters, "Already voted"

        # If reasoning is provided, validate it makes sense with LLM
        if reasoning and len(reasoning) > 10:
            prompt = f"""
Proposal being voted on: "{self.proposal}"
Vote cast: {"YES" if vote else "NO"}
Voter's reasoning: "{reasoning}"

Is this reasoning coherent and relevant to the proposal?
Respond with exactly: VALID or INVALID
"""
            validation = contract_runner.call_llm(prompt).strip().upper()
            if validation == "INVALID":
                return "Vote rejected: reasoning is not coherent with the proposal"

        self.voters[voter] = vote
        if vote:
            self.votes_yes += 1
        else:
            self.votes_no += 1

        return f"Vote recorded: {'YES' if vote else 'NO'}"

    @gl.public.write
    def close_voting(self) -> str:
        """
        Closes voting and returns AI-generated summary of the outcome.
        Only callable by owner.
        """
        assert contract_runner.from_account == self.owner, "Only owner can close voting"
        assert self.is_active, "Already closed"

        self.is_active = False

        prompt = f"""
A vote on the proposal "{self.proposal}" has concluded.
Results: YES={int(self.votes_yes)}, NO={int(self.votes_no)}, Total={int(self.votes_yes + self.votes_no)}

Write a 2-sentence neutral summary of the outcome.
"""
        summary = contract_runner.call_llm(prompt)
        return summary

    @gl.public.write
    def resolve_dispute(self, context_url: str) -> str:
        """
        Uses live web data + LLM to resolve factual disputes about the proposal.

        Args:
            context_url: A URL with relevant information about the proposal topic

        Returns:
            AI-generated resolution based on real-world data
        """
        web_content = contract_runner.get_webpage(context_url, mode="text")

        prompt = f"""
There is a dispute about the following proposal: "{self.proposal}"

Current votes: YES={int(self.votes_yes)}, NO={int(self.votes_no)}

Relevant web content:
---
{web_content[:2000]}
---

Based on this real-world information, provide a fair and neutral assessment
of which position is better supported by facts. Keep it under 3 sentences.
"""
        return contract_runner.call_llm(prompt)
