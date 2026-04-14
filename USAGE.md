# Setup and Usage Guide: Local Agentic System

Welcome to your Always-On Local Agentic System! This guide will walk you through bringing your AI agent online step-by-step. 

By the end of this guide, you will have a secure local AI agent that runs on your machine, remembers what you teach it, and safely executes commands without sending your data to the cloud.

---

## 🛠️ Step 1: Prepare the Brain (Ollama)
First, we need to download the AI model that will act as the "brain" for your agent.

1. Download and install **Ollama** from `https://ollama.com/` if you haven't already.
2. Open a terminal (PowerShell or Command Prompt) and download the Gemma 4 model by running:
   ```bash
   ollama run gemma4:e4b
   ```
   *(Note: This uses the lightweight model suitable for laptops. If you have a powerful GPU, you can try `gemma4:31b` instead).*
3. Once you see the `>>>` prompt, type `/bye` to exit. Ollama is now running correctly in the background!

---

## 🛡️ Step 2: Set Up the Safe Execution Sandbox
We don't want the AI accidently deleting your files! We will use Docker to create a "sandbox" where the agent can safely run commands.

1. Ensure **Docker Desktop** is installed and running on your Windows machine.
2. Open PowerShell as Administrator.
3. Navigate to the project folder and run the setup script to ensure Windows Subsystem for Linux (WSL) is configured:
   ```powershell
   cd path\to\local-agentic-system
   .\scripts\setup_wsl.ps1
   ```
4. Start the Sandbox by running:
   ```powershell
   cd docker
   docker-compose up -d
   ```
   *Your agent now has a safe playground to execute code!*

---

## 🧠 Step 3: Turn on Long-Term Memory
An agent is only as good as its memory. We will set up a Vector Database (ChromaDB) so the agent can read your files.

1. Ensure you have **Python** installed on your computer.
2. Open a normal terminal in the project folder and install the required memory engine packages:
   ```bash
   pip install -r src/memory_engine/requirements.txt
   ```
3. Run the memory engine:
   ```bash
   python src/memory_engine/chroma_client.py
   ```
4. **How to use it daily:** Whenever you add new notes or documentation into the `memory-vault/` folder using an app like Obsidian, just re-run the `chroma_client.py` script. The agent will instantly "learn" everything you just wrote!

---

## 📱 Step 4: Connect the Agent to Telegram (Optional)
If you want to be able to text your agent from your phone:

1. Open Telegram and search for `@BotFather`.
2. Send `/newbot`, give it a name, and copy the **Bot Token** it gives you.
3. Open a terminal in the project folder and set up the bot:
   ```powershell
   # 1. Set your secret token (replace with the one from BotFather)
   $env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
   
   # 2. Set your User ID (so only YOU can command the bot)
   $env:TELEGRAM_AUTHORIZED_USERS="YOUR_TELEGRAM_ID_HERE"
   
   # 3. Install packages and start the bot
   pip install -r src/telegram_bot/requirements.txt
   python src/telegram_bot/main.py
   ```
4. Open Telegram, open a chat with your new bot, send `/start`, and try sending a command like `/exec touch test.txt`. The agent will run this inside its safe Docker sandbox!

---

## 🎯 Daily Workflow Summary
Once everything is set up, your daily workflow looks like this:
1. Make sure **Ollama** and **Docker Desktop** are running.
2. Add facts or project rules to the `memory-vault/` folder.
3. Use the Antigravity IDE (if patched) or OpenClaw to ask the agent to complete tasks. It will utilize the local Ollama brain, read your memory vault, and execute its work inside the Docker sandbox.
