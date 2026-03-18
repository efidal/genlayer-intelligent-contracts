# GenLayer Intelligent Contracts

A collection of Intelligent Contracts built on [GenLayer](https://www.genlayer.com/) — the AI-native blockchain that brings verifiable trust to smart contracts using LLM consensus.

> Deployed and tested on **GenLayer Testnet Bradbury** (March 2026)

---

## What is GenLayer?

GenLayer is a blockchain where smart contracts can:
- Query the live internet
- Process unstructured data (text, images, news)
- Make AI-driven subjective decisions via multi-LLM consensus

Traditional smart contracts are deterministic. GenLayer's **Intelligent Contracts** are not — they can reason.

---

## Contracts in this Repo

| Contract | Description | Status |
|---|---|---|
| [`llm_query.py`](contracts/llm_query.py) | Queries a live URL and extracts information via LLM | Deployed ✅ |
| [`ai_vote.py`](contracts/ai_vote.py) | Multi-option AI voting system with LLM-based result validation | Deployed ✅ |
| [`price_checker.py`](contracts/price_checker.py) | Fetches and validates live asset prices via web + AI consensus | Deployed ✅ |

---

## Getting Started

### Prerequisites
- MetaMask wallet
- GenLayer Testnet added to MetaMask
- Testnet GEN tokens from faucet

### Add GenLayer Testnet to MetaMask

| Field | Value |
|---|---|
| Network Name | GenLayer Testnet Bradbury |
| RPC URL | See [portal](https://portal.genlayer.foundation/) or [Studio](https://studio.genlayer.com/) |
| Chain ID | (shown in Studio on connect) |
| Currency Symbol | GEN |

### Get Testnet Tokens
1. Go to: https://testnet-faucet.genlayer.foundation/
2. Solve captcha → Request Tokens
3. Wait for confirmation in MetaMask

### Deploy a Contract
1. Open [GenLayer Studio](https://studio.genlayer.com/contracts)
2. Connect your wallet
3. Paste or upload a contract from this repo
4. Click **Run and Debug** (▶ play button)
5. Confirm transaction in MetaMask

---

## Tutorial

Full step-by-step guide for Windows users:
👉 [Getting Started on Windows](tutorials/getting-started-windows.md)

---

## Resources

- [GenLayer Docs](https://docs.genlayer.com/)
- [GenLayer Studio](https://studio.genlayer.com/)
- [GenLayer Portal](https://portal.genlayer.foundation/)
- [Validator Setup Guide](https://docs.genlayer.com/validators/setup-guide)
- [Twitter/X](https://x.com/GenLayer)

---

## Author

Built as part of the GenLayer Testnet Bradbury exploration.
