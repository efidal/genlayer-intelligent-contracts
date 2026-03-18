# llm_query.py
# GenLayer Intelligent Contract – Live Web Query via LLM
# Testnet: Bradbury
#
# This contract queries a live URL and uses LLM consensus
# to extract and validate information from unstructured web content.

from genlayer import *


@gl.contract
class WebQueryContract:
    """
    Intelligent Contract that fetches live web content and uses
    LLM consensus to answer questions about it.
    """

    owner: str
    query_count: u256

    def __init__(self) -> None:
        self.owner = contract_runner.from_account
        self.query_count = 0

    @gl.public.view
    def get_owner(self) -> str:
        return self.owner

    @gl.public.view
    def get_query_count(self) -> u256:
        return self.query_count

    @gl.public.write
    def query_webpage(self, url: str, question: str) -> str:
        """
        Fetches content from a URL and answers a question using LLM consensus.

        Args:
            url: The webpage to fetch and analyze
            question: The question to answer based on the page content

        Returns:
            LLM consensus answer as a string
        """
        # Fetch the live web content (non-deterministic)
        web_content = contract_runner.get_webpage(url, mode="text")

        # Build prompt for LLM consensus
        prompt = f"""
You are analyzing the following web content to answer a specific question.

Web content from {url}:
---
{web_content[:3000]}
---

Question: {question}

Answer concisely and factually based only on the content above.
If the answer is not found in the content, respond with: "NOT_FOUND"
"""
        # Run non-deterministic LLM call with consensus
        result = contract_runner.call_llm(prompt)

        self.query_count += 1
        return result

    @gl.public.write
    def check_claim(self, url: str, claim: str) -> bool:
        """
        Verifies whether a claim is supported by content on a given URL.

        Args:
            url: Source URL to verify against
            claim: The statement to verify

        Returns:
            True if claim is supported, False otherwise
        """
        web_content = contract_runner.get_webpage(url, mode="text")

        prompt = f"""
Analyze the following web content and determine if the claim below is TRUE or FALSE.

Web content:
---
{web_content[:3000]}
---

Claim: "{claim}"

Respond with exactly one word: TRUE or FALSE
"""
        result = contract_runner.call_llm(prompt).strip().upper()
        self.query_count += 1
        return result == "TRUE"
