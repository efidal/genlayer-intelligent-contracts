# Anleitung: Repo auf GitHub pushen

## Einmalig: Git installieren (falls nicht vorhanden)
Download: https://git-scm.com/download/win → installieren → PC neu starten

---

## Schritt 1 – Neues Repo auf GitHub erstellen

1. Gehe zu: https://github.com/new
2. Repository name: `genlayer-intelligent-contracts`
3. Description: `Intelligent Contracts built on GenLayer Testnet Bradbury — AI-native blockchain`
4. Visibility: **Public** (wichtig für Contributions!)
5. **KEIN** README hinzufügen (haben wir schon)
6. Klicke **Create repository**

---

## Schritt 2 – Terminal öffnen und pushen

Drücke `Win + R` → tippe `cmd` → Enter

Dann diese Befehle **nacheinander** kopieren und ausführen:

```bash
cd "c:\Airdrop\GenLayer\genlayer-intelligent-contracts"

git init
git add .
git commit -m "Initial commit: GenLayer Intelligent Contracts + Windows Tutorial"
git branch -M main
git remote add origin https://github.com/efidal/genlayer-intelligent-contracts.git
git push -u origin main
```

GitHub fragt nach Login → Browser öffnet sich → einloggen → fertig.

---

## Schritt 3 – Repo-Link kopieren

Nach dem Push ist dein Repo live unter:
**https://github.com/efidal/genlayer-intelligent-contracts**

---

## Schritt 4 – Sofort 3 Contributions submitten

### Contribution 1 – Tutorial
```
Category:    Builders
Title:       Getting Started with GenLayer on Windows – Full Tutorial
Description: Step-by-step tutorial for Windows users to deploy their first
             Intelligent Contract on GenLayer Testnet Bradbury. Covers
             MetaMask setup, faucet, Studio deploy, and Portal submission.
Link:        https://github.com/efidal/genlayer-intelligent-contracts/blob/main/tutorials/getting-started-windows.md
```

### Contribution 2 – Smart Contracts Collection
```
Category:    Builders
Title:       3 Intelligent Contracts deployed on Bradbury Testnet
Description: Deployed llm_query.py (live web query), ai_vote.py (AI voting
             system), and price_checker.py (decentralized price oracle) on
             GenLayer Testnet Bradbury via GenLayer Studio.
Link:        https://github.com/efidal/genlayer-intelligent-contracts
Tx Hash:     [paste your tx hash from Studio]
```

### Contribution 3 – Open Source Repo
```
Category:    Builders
Title:       Open-source GenLayer contract repo for community
Description: Published a public GitHub repository with Intelligent Contracts
             and tutorial to help new developers onboard to GenLayer.
Link:        https://github.com/efidal/genlayer-intelligent-contracts
```

---

## Erwartete Points

| Contribution | Erwartete Points |
|---|---|
| Windows Tutorial | 100–260 pts |
| 3 Contracts deployed | 100–500 pts |
| Open-source Repo | 50–150 pts |
| **Total** | **250–910 pts** |
