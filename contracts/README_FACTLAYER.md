# FactLayer — Decentralized Fact-Checking Protocol

> GenLayer Hackathon Submission | Testnet Bradbury | March 2026

## What is FactLayer?

FactLayer is a decentralized fact-checking protocol built on GenLayer.

Anyone can submit a claim and a source URL. Multiple AI validators independently fetch the URL, analyze the content, and vote on the verdict. GenLayer's LLM consensus mechanism produces a final, tamper-proof result stored on-chain.

**No central authority. No single AI model. Pure decentralized truth.**

## How It Works

```
User submits:  "Bitcoin was created in 2009"  +  https://wikipedia.org/wiki/Bitcoin
                              ↓
         GenLayer Validators (each runs independently):
         [GPT-4] fetches URL → analyzes → votes TRUE
         [Claude] fetches URL → analyzes → votes TRUE
         [Llama] fetches URL → analyzes → votes TRUE
                              ↓
              Consensus: ✅ TRUE (Confidence: HIGH)
                              ↓
                  Result stored permanently on-chain
```

## Key Functions

| Function | Description |
|---|---|
| `submit_claim(claim, url)` | Submit a claim for verification |
| `verify_claim(claim_id)` | Run AI consensus verification |
| `submit_and_verify(claim, url)` | One-step: submit + verify |
| `challenge_verdict(claim_id, new_url)` | Challenge with new evidence |
| `get_claim(claim_id)` | Get full details of a claim |
| `get_verdict(claim_id)` | Get just the verdict |

## Example Usage

```python
# Submit and verify in one step
contract.submit_and_verify(
    claim="The Eiffel Tower is located in Paris, France",
    source_url="https://en.wikipedia.org/wiki/Eiffel_Tower"
)
# → "Claim #0 verdict: TRUE (Confidence: HIGH)"

# Challenge a verdict with new evidence
contract.challenge_verdict(
    claim_id=0,
    new_source_url="https://www.toureiffel.paris/en"
)
```

## Why GenLayer Makes This Possible

Traditional blockchains cannot do this — they have no access to the internet and cannot make subjective judgments.

GenLayer's Intelligent Contracts can:
- **Fetch live web content** — no centralized oracle needed
- **Run LLM inference** — AI reasoning on-chain
- **Reach consensus** — multiple validators agree on subjective outcomes

FactLayer would be impossible on Ethereum, Solana, or any other chain.

## Deployed On

- Network: GenLayer Testnet Bradbury
- Author: [@efidal](https://github.com/efidal)
