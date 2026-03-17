# Getting Started with GenLayer on Windows
### Deploy your first Intelligent Contract in under 30 minutes

> Written by [@efidal](https://github.com/efidal) | Tested on Windows 11 | Testnet: Bradbury (March 2026)

---

## What You'll Learn

By the end of this tutorial you will have:
- Added the GenLayer testnet to MetaMask
- Claimed free testnet GEN tokens
- Deployed your first Intelligent Contract via GenLayer Studio
- Submitted your first contribution to the GenLayer Portal

---

## Prerequisites

- **Browser:** Chrome or Firefox with MetaMask extension installed
- **Wallet:** MetaMask set up with at least one account
- **Time:** ~20–30 minutes

No coding experience required for the basic steps. Python knowledge helps for writing custom contracts.

---

## Step 1 – Add GenLayer Testnet to MetaMask

1. Open MetaMask → Click the network dropdown at the top
2. Click **Add Network** → **Add a network manually**
3. Fill in the network details (find current RPC in [GenLayer Studio](https://studio.genlayer.com/) after connecting your wallet — it auto-prompts you to add the network)

**Alternative (easiest):**
- Open [GenLayer Studio](https://studio.genlayer.com/)
- Click **Connect Wallet**
- MetaMask will automatically prompt you to add the GenLayer network
- Click **Approve**

---

## Step 2 – Claim Testnet GEN Tokens (Faucet)

1. Go to: **https://testnet-faucet.genlayer.foundation/**
2. Copy your MetaMask wallet address (0x...)
3. Paste it in the faucet field
4. Solve the captcha
5. Click **Request Tokens**
6. Wait 30–60 seconds → tokens appear in MetaMask

> If the main faucet is slow, try: https://genlayer-testnet.hub.caldera.xyz/

You only need a small amount (0.1–1 GEN) to deploy contracts — testnet gas is minimal.

---

## Step 3 – Deploy Your First Intelligent Contract

### Option A – Use an Example Contract (Easiest, 5 minutes)

1. Go to: **https://studio.genlayer.com/contracts**
2. Click **Connect Wallet** → approve in MetaMask
3. In the left panel, you'll see example contracts — click any one (e.g. `llm_erc20` or `storage`)
4. Click the **▶ Run and Debug** button on the right
5. A deploy dialog appears → click **Deploy**
6. Confirm the transaction in MetaMask (tiny gas fee)
7. Wait for **"Contract deployed successfully"** message
8. **Copy the transaction hash (Tx Hash)** — you'll need it for the Portal contribution

### Option B – Deploy a Custom Contract from This Repo

1. In GenLayer Studio, click **New Contract** or **+**
2. Copy the contents of any `.py` file from the [`contracts/`](../contracts/) folder in this repo
3. Paste into the Studio editor
4. Click **▶ Run and Debug** → **Deploy**
5. Confirm in MetaMask → copy Tx Hash

---

## Step 4 – Submit Your Contribution to the Portal

This is where you actually earn Points.

1. Go to: **https://portal.genlayer.foundation/**
2. Connect your wallet (same MetaMask account)
3. Click **Submit Contribution** or **Contribute**
4. Fill in the form:

```
Category:     Builders
Title:        Deployed first Intelligent Contract on GenLayer Testnet
Description:  Deployed [contract name] on GenLayer Testnet Bradbury using
              GenLayer Studio. The contract demonstrates [what it does].
Link:         [URL to your contract in Studio, or this GitHub repo]
Tx Hash:      [paste the transaction hash from Step 3]
```

5. Attach a screenshot of the successful deployment
6. Click **Submit**

Points are awarded after manual review (usually within 24–72 hours).

---

## Step 5 – Complete Your Profile (More Points)

In the Portal, click your profile icon → **Edit Profile**:

- [ ] Connect GitHub account
- [ ] Star the GenLayer GitHub repos
- [ ] Connect Twitter/X
- [ ] Connect Discord

Each completed item may trigger small instant rewards.

---

## Bonus: What Makes Intelligent Contracts Different?

A traditional Ethereum contract can only work with data already on-chain.

A GenLayer **Intelligent Contract** can do this:

```python
# Traditional smart contract — only on-chain data
def get_balance(address):
    return balances[address]  # ✅ deterministic

# GenLayer Intelligent Contract — real world + AI
def check_news_sentiment(url):
    content = contract_runner.get_webpage(url)  # fetches live website
    result = contract_runner.call_llm(          # multiple AI validators vote
        f"Is this news positive or negative? {content}"
    )
    return result  # consensus answer from multiple LLMs ✅
```

Multiple validator nodes run the same LLM query independently and reach consensus — so the result is decentralized and trustless, even though it uses AI.

---

## Troubleshooting (Windows)

| Problem | Solution |
|---|---|
| MetaMask won't connect to Studio | Disable other wallet extensions temporarily |
| Faucet says "already claimed" | Wait 24h or use the alternate faucet URL |
| Tx stuck pending | Speed up in MetaMask (increase gas) or wait 5 min |
| Studio shows blank page | Hard refresh: Ctrl+Shift+R |
| Contract deploy fails | Check you have GEN tokens; re-claim faucet if needed |

---

## Next Steps

- Explore the [GenLayer Docs](https://docs.genlayer.com/) to write more complex contracts
- Submit more contributions to the [Portal](https://portal.genlayer.foundation/)
- Apply for the **Validator waitlist** to earn 1,800–2,200 pts/month
- Join the [GenLayer Discord](https://discord.gg/genlayer) for support

---

## Resources

- [GenLayer Portal](https://portal.genlayer.foundation/?ref=6TWD49RC)
- [GenLayer Studio](https://studio.genlayer.com/)
- [Official Docs](https://docs.genlayer.com/)
- [Validator Guide](https://docs.genlayer.com/validators/setup-guide)
- [GenLayer on X](https://x.com/GenLayer)

---

*Found this helpful? Share it and help others get started on GenLayer.*
