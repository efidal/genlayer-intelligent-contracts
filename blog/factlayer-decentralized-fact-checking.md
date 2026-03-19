# FactLayer: Why Decentralized Fact-Checking Is Only Possible on GenLayer

*Published as part of the GenLayer Testnet Bradbury Hackathon — March 2026*

---

## The Problem: Who Decides What's True?

Misinformation is one of the defining problems of our era. A claim goes viral. Millions share it. By the time it's debunked, the damage is done.

Existing fact-checking solutions have a fundamental flaw: **they rely on a central authority to decide what's true.**

- Fact-checking websites employ human editors — slow, expensive, biased
- Social media platforms use opaque AI moderation — untransparent, easily gamed
- Community-based systems like Wikipedia are better, but still controlled by a small group of editors

What if fact-checking could be **decentralized, transparent, and governed by consensus** — with no single point of control?

That's what I built with **FactLayer**.

---

## What is FactLayer?

FactLayer is a decentralized fact-checking protocol built as an Intelligent Contract on [GenLayer](https://genlayer.com/) — the AI-native blockchain.

The flow is simple:

1. Anyone submits a **claim** and a **source URL**
2. Multiple AI validators independently **fetch the source URL** and analyze the content
3. Each validator votes: **TRUE**, **FALSE**, or **UNVERIFIABLE**
4. GenLayer's consensus mechanism aggregates the votes
5. The final verdict — and the AI's reasoning — is stored **permanently on-chain**

No central authority. No single AI model. No way to manipulate the result after the fact.

---

## Why This Is Impossible on Other Blockchains

This is where GenLayer's architecture becomes critical. Let me explain why FactLayer cannot exist on Ethereum, Solana, or any other traditional blockchain.

### Problem 1: Smart Contracts Cannot Access the Internet

Traditional smart contracts are **sandboxed**. They can only read data that has already been written to the blockchain. They cannot fetch a Wikipedia article, read a news story, or query any external URL.

The common workaround is an **oracle** — a trusted third party that fetches web data and writes it to the chain. But this just moves the trust problem: now you're trusting the oracle.

**GenLayer solves this natively.** Intelligent Contracts can call `gl.get_webpage(url)` directly. Each validator fetches the URL independently during consensus. There is no oracle, no trusted third party.

```python
# This is real GenLayer code — no oracle needed
web_content = gl.get_webpage(source_url, mode="text")
```

### Problem 2: AI Inference Cannot Run On-Chain

Even if a traditional chain had web access, you couldn't run an LLM to analyze the content. Smart contracts execute deterministically with a fixed gas model — running a neural network is computationally impossible.

**GenLayer solves this natively.** Validators run LLM inference as part of the consensus process. The `gl.eq_principle_prompt_comparative()` function sends a prompt to the validator's LLM and reaches consensus across different models.

```python
result = gl.eq_principle_prompt_comparative(
    prompt,
    principle="The fact-checker should reach the same verdict when analyzing the same claim and source."
)
```

### Problem 3: Non-Determinism Breaks Consensus

Here's the deep problem: if you ask GPT-4 the same question twice, you might get different answers. Traditional blockchains require **every validator to produce the exact same result** — otherwise they can't reach consensus.

GenLayer introduces **Optimistic Democracy** — a consensus mechanism designed specifically for non-deterministic AI outputs. Validators don't need to agree on the exact wording of the response. They need to agree on the **semantic outcome** (TRUE/FALSE/UNVERIFIABLE). The `eq_principle_prompt_comparative` function handles this.

---

## How FactLayer Works — Under the Hood

Here is the full verification flow:

```
User calls: submit_and_verify("Bitcoin was created in 2009", "https://en.wikipedia.org/wiki/Bitcoin")
                                        |
                              GenLayer receives transaction
                                        |
               ┌────────────────────────┼────────────────────────┐
               |                        |                        |
         Validator A              Validator B              Validator C
         (GPT-4)                  (Claude)                 (Llama)
               |                        |                        |
         fetches URL             fetches URL             fetches URL
               |                        |                        |
         runs LLM                runs LLM                runs LLM
               |                        |                        |
         votes: TRUE             votes: TRUE             votes: TRUE
               |                        |                        |
               └────────────────────────┼────────────────────────┘
                                        |
                              Consensus: TRUE (HIGH confidence)
                                        |
                    Stored on-chain: verdict + confidence + reason
```

The prompt I wrote instructs the LLM to respond in a structured format:

```
VERDICT: TRUE
CONFIDENCE: HIGH
REASON: The Wikipedia article explicitly states Bitcoin was introduced in 2008 and the first block was mined in January 2009.
```

FactLayer parses this response and stores all three fields on-chain. The **reason field** is particularly powerful — it makes the AI's decision process fully transparent and auditable.

---

## The Challenge Mechanism

One of FactLayer's most interesting features is `challenge_verdict()`. If you disagree with a verdict, you can submit a **new source URL** as counter-evidence.

The contract re-runs the verification with both the original and new source, producing an updated verdict. The original source is always preserved on-chain — you can trace the full history of a claim.

This creates a **living fact-check** that improves as more evidence is added.

```python
# A claim was marked UNVERIFIABLE — you find a better source
contract.challenge_verdict(
    claim_id=3,
    new_source_url="https://arxiv.org/abs/..."
)
# → "Claim #3: UNVERIFIABLE → TRUE (CHANGED, Confidence: HIGH)"
```

---

## The On-Chain Data Model

Every claim stores:

| Field | Type | Description |
|---|---|---|
| `claim` | string | The statement to verify |
| `source` | string | The URL used for verification |
| `verdict` | string | TRUE / FALSE / UNVERIFIABLE |
| `confidence` | string | HIGH / MEDIUM / LOW |
| `reason` | string | One-sentence LLM explanation |
| `submitter` | address | Wallet that submitted the claim |
| `verified` | bool | Whether verification has run |

This data is **permanent and immutable**. No one can go back and change a verdict after the fact. Every claim is a timestamped, cryptographically secured record of what an AI consensus determined at a specific point in time.

---

## What This Means for the Real World

The implications go beyond a hackathon demo.

**News verification**: Journalists submit breaking claims before publishing. The protocol returns a confidence-weighted verdict with source attribution in seconds.

**Social media integration**: A browser extension could submit viral claims to FactLayer and display verdicts inline — crowd-sourced, AI-verified, on-chain.

**Legal discovery**: Claims made in legal proceedings could be submitted for automated preliminary fact-checking with full audit trails.

**Academic citation checking**: Verify whether a cited source actually supports the claim being made.

All of these applications share one property: they require **web access + AI reasoning + tamper-proof storage**. That combination only exists on GenLayer.

---

## Try It Yourself

The full contract source code is open-source:

**GitHub**: [github.com/efidal/genlayer-intelligent-contracts](https://github.com/efidal/genlayer-intelligent-contracts)

**Contract**: `contracts/factlayer.py`

**Frontend**: `frontend/index.html` — open it in a browser, connect Rabby/MetaMask to GenLayer Testnet Bradbury, and submit a claim.

Key functions:

```python
# One-step: submit + verify
contract.submit_and_verify(claim, source_url)

# Two-step: submit first, verify later
claim_id = contract.submit_claim(claim, source_url)
verdict   = contract.verify_claim(claim_id)

# Challenge with new evidence
contract.challenge_verdict(claim_id, new_source_url)

# Read all claims (for frontends)
all_claims = contract.get_all_claims()
```

---

## Conclusion

FactLayer demonstrates what becomes possible when blockchains can reason.

The combination of live web access, LLM inference, and consensus is not a feature you can bolt onto an existing chain. It requires a fundamentally different architecture — one that GenLayer has built from the ground up.

We are at the very beginning of what AI-native blockchains can do. Fact-checking is one application. The same pattern — *fetch real-world data, reason about it, reach consensus, store the result permanently* — applies to legal contracts, insurance claims, prediction markets, content moderation, and more.

GenLayer makes this possible today, on testnet, with working code.

---

*Built by [@efidal](https://github.com/efidal) | Twitter: [@MehdiFidal](https://x.com/MehdiFidal)*
*GenLayer Testnet Bradbury Hackathon — March 2026*
