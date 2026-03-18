# GenLayer Complete Onboarding Guide — Do It Right the First Time
### Avoid the common pitfalls and earn maximum points from day one

> March 2026 | Based on real onboarding experience

---

## Why This Guide Exists

The official documentation does not tell you the correct **order** of steps. If you do things in the wrong sequence, you will hit blockers like:

- ❌ "You must complete the Builder Welcome Journey before submitting builder contributions"
- ❌ "Error deploying contract" (Studio whitelist not approved yet)
- ❌ Validator contributions available but Builder contributions locked
- ❌ Spending time trying to add GenLayer network manually when the Portal does it automatically

This guide gives you the exact order that works — learned the hard way.

---

## Overview: The Correct Order

```
1. Create accounts (GitHub + Portal)
2. Complete your Portal profile
3. Complete the Builder Journey (in the right order!)
4. Request Studio whitelist
5. Submit Validator contributions (while waiting for whitelist)
6. Deploy contract (after whitelist approval)
7. Submit Builder contributions
8. Share your referral link
```

---

## Step 1 — Prepare Your Accounts

Before touching the Portal, make sure you have:

- [ ] A **Web3 wallet** installed — Rabby or MetaMask (browser extension)
- [ ] A **GitHub account** — https://github.com
- [ ] A **Twitter/X account** (optional but recommended for Community outreach)
- [ ] A **Discord account** (optional but recommended)

---

## Step 2 — Join the Portal and Complete Your Profile

1. Go to: **https://portal.genlayer.foundation/**
2. Click **Connect Wallet** → approve in your wallet
3. Click your profile icon (top right) → **Edit Profile**
4. Fill in everything:
   - Connect GitHub account ← **critical, do this first**
   - Connect Twitter/X
   - Connect Discord
   - Add a profile picture

> **Why this order matters:** GitHub must be connected before the Builder Journey can verify your repo stars and contributions.

---

## Step 3 — Complete the Builder Journey (correct order)

Go to: **Portal → Builders → Apply for the role**

You will see a checklist. Complete them **in this exact order:**

### 3a. Star the Boilerplate Repo
- Click **"Star Repo"** → GitHub opens automatically
- Click the ⭐ Star button on the GitHub page
- Go back to Portal → click the 🔄 refresh icon next to the step
- Wait for the green checkmark

> **Common mistake:** People skip this and try to deploy first. The journey won't complete without it.

### 3b. Add GenLayer Testnet Chain
- Click **"Add Network"**
- Your wallet will show a popup — click **Approve**
- The step turns green automatically

> **Important:** Do NOT try to add the network manually through Chainlist or other tools. The Portal button adds the correct network automatically. Manual attempts will add the wrong network (e.g. AgentLayer instead of GenLayer).

### 3c. Add Studio Network
- Click the second **"Add Network"** button
- Approve in your wallet

### 3d. Request Studio Whitelist
- Click **"Open Studio"** → https://studio.genlayer.com/
- Connect your wallet in the Studio
- You will see a whitelist request prompt — **submit it immediately**
- You cannot deploy contracts until the whitelist is approved

> **This is the main blocker.** Whitelist approval takes time (hours to days). Do NOT wait for it before doing other things — continue with Step 4 below.

---

## Step 4 — Earn Points While Waiting for Whitelist

While your Studio whitelist is being reviewed, you can still earn points as a **Validator**.

Go to: **Portal → Submit a contribution → Validator tab**

These contribution types do NOT require the Builder Journey or Studio access:

| Type | What to submit | Points |
|---|---|---|
| **Educational Content** | Tutorial you wrote, GitHub repo with contracts | 20–400 pts |
| **Community Outreach** | Twitter post, Discord post with your referral link | 20–200 pts |
| **Blog Post** | Article explaining GenLayer, GitHub repo | 20–200 pts |
| **Documentation** | Improved docs, README files | 20–200 pts |

> **Key insight:** The Validator contribution tab is separate from the Builder tab and does NOT require the Builder Welcome Journey. Use it immediately.

---

## Step 5 — Get Your Referral Link

Go to: **Portal → How it works** (scroll to bottom) → click **"Referral link"**

Copy your link: `https://portal.genlayer.foundation/?ref=YOURCODE`

Share it everywhere:
- Twitter/X thread explaining GenLayer
- Discord servers (crypto, web3, AI groups)
- Telegram groups

> **Why this is important:** You earn **10% of every point** your referrals earn — forever, with no cap. This is the strongest passive income in the entire ecosystem.

---

## Step 6 — Deploy Your First Contract (after whitelist approval)

Once you receive whitelist approval (check your email or Studio):

1. Go to: **https://studio.genlayer.com/contracts**
2. Connect your wallet
3. Select a contract from the left panel — start with **`storage.py`** (simplest, no LLM needed)
4. Click **▶ Run and Debug**
5. Click **Deploy** → confirm in your wallet
6. Copy the **transaction hash (Tx Hash)**

> **Why storage.py first:** Contracts that use LLM (like llm_erc20.py) require an AI provider configured. storage.py works without any API key and is the fastest way to complete the Builder Journey.

---

## Step 7 — Complete the Builder Journey

After deploying a contract, go back to **Portal → Builder Journey** → the "Deploy your first contract" step turns green → click **"Complete Builder Journey"**.

Now you can submit **Builder contributions** which have much higher point potential (up to 4,000 pts).

---

## Step 8 — Submit Builder Contributions

Now submit everything you built as Builder contributions:

**Contribution 1 — Educational Content (20–400 pts)**
```
Type:        Builder → Educational Content
Description: [Your tutorial description]
Evidence:    [Link to your GitHub tutorial or article]
```

**Contribution 2 — Projects & Milestones (20–4,000 pts)**
```
Type:        Builder → Projects & Milestones
Description: [Your project description]
Evidence:    [Link to your deployed contract or GitHub repo]
Tx Hash:     [Your deployment transaction hash]
```

---

## Common Mistakes to Avoid

| Mistake | What happens | Solution |
|---|---|---|
| Submitting Builder contribution before completing Builder Journey | "You must complete the Builder Welcome Journey" error | Complete the journey first (Steps 3a–3d) |
| Trying to add GenLayer network manually via Chainlist | Adds wrong network (AgentLayer, etc.) | Use the "Add Network" button in the Portal |
| Waiting for Studio whitelist before doing anything | Wastes days | Submit Validator contributions immediately while waiting |
| Deploying llm_erc20.py as first contract | "Error deploying contract" (no LLM API key) | Deploy storage.py first instead |
| Skipping the refresh icon after starring a repo | Step stays unchecked | Always click 🔄 after completing each step |

---

## Points Summary — What to Expect

| Activity | When | Points |
|---|---|---|
| Profile complete | Day 1 | ~20 pts |
| Validator contributions (3x) | Day 1 | 60–800 pts |
| Builder Journey complete | Day 1–3 | unlocks Builder |
| Builder contributions (2x) | After journey | 40–4,400 pts |
| Referral (per active referral) | Ongoing | 10% lifetime |
| Hackathon project | Quarterly | 1,000–4,000 pts |

---

## Quick Reference — All Important Links

| Resource | URL |
|---|---|
| Portal | https://portal.genlayer.foundation/ |
| Studio | https://studio.genlayer.com/ |
| Faucet | https://testnet-faucet.genlayer.foundation/ |
| Docs | https://docs.genlayer.com/ |
| Validator Guide | https://docs.genlayer.com/validators/setup-guide |
| Twitter/X | https://x.com/GenLayer |

---

*Based on hands-on experience onboarding to GenLayer Testnet Bradbury in March 2026.*
