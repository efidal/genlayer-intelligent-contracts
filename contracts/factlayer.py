# factlayer.py
# GenLayer Intelligent Contract — Decentralized Fact-Checking Protocol
# Hackathon: Testnet Bradbury
#
# Anyone can submit a claim + source URL.
# Multiple AI validators independently verify the claim using live web data.
# LLM consensus determines: TRUE / FALSE / UNVERIFIABLE
#
# This demonstrates GenLayer's core power:
# → Live web fetching (no oracles needed)
# → Multi-LLM consensus (decentralized truth)
# → Subjective AI decisions on-chain

from genlayer import *


@gl.contract
class FactLayer(gl.Contract):
    """
    Decentralized Fact-Checking Protocol powered by LLM consensus.

    Flow:
    1. Anyone submits a claim + source URL
    2. GenLayer validators independently fetch the URL and evaluate the claim
    3. LLM consensus produces a verified verdict: TRUE / FALSE / UNVERIFIABLE
    4. Result is stored permanently on-chain
    """

    owner: str
    claim_count: u256
    claims: TreeMap[u256, str]          # claim_id → claim text
    sources: TreeMap[u256, str]         # claim_id → source URL
    verdicts: TreeMap[u256, str]        # claim_id → "TRUE" / "FALSE" / "UNVERIFIABLE"
    confidence: TreeMap[u256, str]      # claim_id → confidence level
    submitters: TreeMap[u256, str]      # claim_id → submitter address
    verified: TreeMap[u256, bool]       # claim_id → has been verified

    def __init__(self) -> None:
        self.owner = gl.message.sender_address
        self.claim_count = u256(0)

    # ─── READ FUNCTIONS ────────────────────────────────────────────────────────

    @gl.public.view
    def get_claim(self, claim_id: u256) -> dict:
        """Returns all details about a specific claim."""
        return {
            "id": int(claim_id),
            "claim": self.claims[claim_id] if claim_id in self.claims else "",
            "source": self.sources[claim_id] if claim_id in self.sources else "",
            "verdict": self.verdicts[claim_id] if claim_id in self.verdicts else "PENDING",
            "confidence": self.confidence[claim_id] if claim_id in self.confidence else "",
            "submitter": self.submitters[claim_id] if claim_id in self.submitters else "",
            "verified": self.verified[claim_id] if claim_id in self.verified else False,
        }

    @gl.public.view
    def get_total_claims(self) -> u256:
        """Returns total number of claims submitted."""
        return self.claim_count

    @gl.public.view
    def get_verdict(self, claim_id: u256) -> str:
        """Returns the verdict for a claim: TRUE / FALSE / UNVERIFIABLE / PENDING"""
        if claim_id not in self.verdicts:
            return "PENDING"
        return self.verdicts[claim_id]

    # ─── WRITE FUNCTIONS ───────────────────────────────────────────────────────

    @gl.public.write
    def submit_claim(self, claim: str, source_url: str) -> u256:
        """
        Submit a claim for fact-checking.

        Args:
            claim: The statement to verify (e.g. "Bitcoin was created in 2009")
            source_url: A public URL that contains relevant information

        Returns:
            claim_id: The ID assigned to this claim
        """
        assert len(claim) >= 10, "Claim must be at least 10 characters"
        assert len(claim) <= 500, "Claim must be under 500 characters"
        assert source_url.startswith("http"), "Source must be a valid URL"

        claim_id = self.claim_count
        self.claims[claim_id] = claim
        self.sources[claim_id] = source_url
        self.submitters[claim_id] = gl.message.sender_address
        self.verified[claim_id] = False
        self.claim_count = u256(int(self.claim_count) + 1)

        return claim_id

    @gl.public.write
    def verify_claim(self, claim_id: u256) -> str:
        """
        Verify a submitted claim using live web data + LLM consensus.

        This is the core function — GenLayer validators independently:
        1. Fetch the source URL
        2. Analyze the content
        3. Vote on TRUE / FALSE / UNVERIFIABLE

        Args:
            claim_id: ID of the claim to verify

        Returns:
            verdict: "TRUE", "FALSE", or "UNVERIFIABLE"
        """
        assert claim_id in self.claims, "Claim does not exist"

        claim = self.claims[claim_id]
        source_url = self.sources[claim_id]

        # Fetch live web content (non-deterministic — each validator fetches independently)
        web_content = gl.get_webpage(source_url, mode="text")

        # LLM consensus prompt
        prompt = f"""You are a professional fact-checker. Your job is to verify whether a claim is TRUE or FALSE based on the provided source content.

CLAIM TO VERIFY:
"{claim}"

SOURCE CONTENT (from {source_url}):
---
{web_content[:3000]}
---

INSTRUCTIONS:
1. Read the source content carefully
2. Determine if the claim is supported, contradicted, or cannot be verified from this source
3. Respond in this exact format:

VERDICT: [TRUE or FALSE or UNVERIFIABLE]
CONFIDENCE: [HIGH or MEDIUM or LOW]
REASON: [One sentence explaining your verdict]

Rules:
- TRUE: The source clearly supports the claim
- FALSE: The source clearly contradicts the claim
- UNVERIFIABLE: The source does not contain enough information to verify the claim
"""

        result = gl.eq_principle_prompt_comparative(
            prompt,
            principle="The fact-checker should reach the same verdict when analyzing the same claim and source content."
        )

        # Parse the LLM response
        verdict = "UNVERIFIABLE"
        confidence_level = "LOW"

        result_upper = result.upper()
        if "VERDICT: TRUE" in result_upper:
            verdict = "TRUE"
        elif "VERDICT: FALSE" in result_upper:
            verdict = "FALSE"
        else:
            verdict = "UNVERIFIABLE"

        if "CONFIDENCE: HIGH" in result_upper:
            confidence_level = "HIGH"
        elif "CONFIDENCE: MEDIUM" in result_upper:
            confidence_level = "MEDIUM"
        else:
            confidence_level = "LOW"

        # Store the verified result
        self.verdicts[claim_id] = verdict
        self.confidence[claim_id] = confidence_level
        self.verified[claim_id] = True

        return f"{verdict} (Confidence: {confidence_level})"

    @gl.public.write
    def submit_and_verify(self, claim: str, source_url: str) -> str:
        """
        Convenience function: submit a claim AND verify it in one transaction.

        Args:
            claim: The statement to verify
            source_url: A public URL with relevant information

        Returns:
            Full result with claim ID and verdict
        """
        claim_id = self.submit_claim(claim, source_url)
        verdict = self.verify_claim(claim_id)
        return f"Claim #{int(claim_id)} verdict: {verdict}"

    @gl.public.write
    def challenge_verdict(self, claim_id: u256, new_source_url: str) -> str:
        """
        Challenge an existing verdict with a new source URL.
        Re-runs verification with additional evidence.

        Args:
            claim_id: ID of the claim to challenge
            new_source_url: A new URL with additional evidence

        Returns:
            New verdict after re-verification
        """
        assert claim_id in self.claims, "Claim does not exist"
        assert self.verified[claim_id], "Claim has not been verified yet"

        claim = self.claims[claim_id]
        original_source = self.sources[claim_id]
        old_verdict = self.verdicts[claim_id]

        # Fetch both sources
        original_content = gl.get_webpage(original_source, mode="text")
        new_content = gl.get_webpage(new_source_url, mode="text")

        prompt = f"""You are a professional fact-checker re-evaluating a claim after new evidence was submitted.

CLAIM:
"{claim}"

ORIGINAL SOURCE ({original_source}):
---
{original_content[:1500]}
---

NEW EVIDENCE SOURCE ({new_source_url}):
---
{new_content[:1500]}
---

PREVIOUS VERDICT: {old_verdict}

Based on BOTH sources combined, what is your final verdict?

Respond in this exact format:
VERDICT: [TRUE or FALSE or UNVERIFIABLE]
CONFIDENCE: [HIGH or MEDIUM or LOW]
REASON: [One sentence]
CHANGED: [YES or NO - did the new evidence change the verdict?]
"""

        result = gl.eq_principle_prompt_comparative(
            prompt,
            principle="The fact-checker should reach the same verdict when analyzing the same claim and sources."
        )

        # Parse result
        new_verdict = old_verdict
        confidence_level = "LOW"

        result_upper = result.upper()
        if "VERDICT: TRUE" in result_upper:
            new_verdict = "TRUE"
        elif "VERDICT: FALSE" in result_upper:
            new_verdict = "FALSE"
        else:
            new_verdict = "UNVERIFIABLE"

        if "CONFIDENCE: HIGH" in result_upper:
            confidence_level = "HIGH"
        elif "CONFIDENCE: MEDIUM" in result_upper:
            confidence_level = "MEDIUM"

        self.verdicts[claim_id] = new_verdict
        self.confidence[claim_id] = confidence_level
        self.sources[claim_id] = new_source_url  # update to latest source

        changed = "CHANGED" if new_verdict != old_verdict else "UNCHANGED"
        return f"Claim #{int(claim_id)}: {old_verdict} → {new_verdict} ({changed}, Confidence: {confidence_level})"
