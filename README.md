# Always-On Local Agentic System

A fully open-source, absolutely private architecture for running localized, always-on AI agents (with Google Antigravity & OpenClaw) utilizing local Gemma 4 instances. 

This framework prioritizes **data sovereignty** and **verifiable autonomy**, ensuring that sensitive developmental operations and agent thinking are contained entirely within your local hardware and isolated sandboxes.

## Features at a Glance
- 🧠 **Local Cognitive Engine**: Powered by Ollama and **Gemma 4**, ensuring no code leaves your machine.
- 🛡️ **Secure Execution**: Code and terminal commands written by the agent are executed in an isolated WSL2 / Docker Sandbox.
- 💾 **Triple-Layer Memory**: Built on ChromaDB vector retrieval and Obsidian so your agent "remembers" your project structures across sessions.
- 📱 **Telegram Orchestration**: Securely message your agent from your phone via an encrypted end-to-end bot interface.

---

## 🚀 Setup and Usage Guide

Welcome to your new Always-On Local Agent! By following these steps, you will bring your secure AI agent online.

### 🛠️ Step 1: Prepare the Brain (Ollama)
First, we need to download the AI model that will act as the "brain".

1. Download and install **Ollama** from `https://ollama.com/` if you haven't already.
2. Open a terminal (PowerShell or Command Prompt) and download the Gemma 4 model:
   ```bash
   ollama run gemma4:e4b
   ```
   *(Note: This uses the lightweight model. If you have a powerful GPU with VRAM, try `gemma4:31b` instead).*
3. Once you see the `>>>` prompt, type `/bye` to exit. Ollama is now running as an API service in the background!

### 🛡️ Step 2: Set Up the Safe Execution Sandbox
We don't want the AI accidently deleting your host system's files! We will use Docker to create a specific "sandbox".

1. Ensure **Docker Desktop** is installed and running on your Windows machine.
2. Open PowerShell as Administrator.
3. Navigate to this project folder and run the system setup script to ensure Windows Subsystem for Linux (WSL) is configured correctly:
   ```powershell
   cd path\to\local-agentic-system
   .\scripts\setup_wsl.ps1
   ```
4. Start the Sandbox:
   ```powershell
   cd docker
   docker-compose up -d
   ```
   *Your agent now has a safe, isolated playground to execute code!*

### 🧠 Step 3: Turn on Long-Term Memory
An agent is only as good as its memory. We use ChromaDB to let the agent read your project wikis and docs.

1. Ensure you have **Python** installed on your computer.
2. Open a normal terminal in the project folder and install the required packages:
   ```bash
   pip install -r src/memory_engine/requirements.txt
   ```
3. Run the memory engine script to index your knowledge base:
   ```bash
   python src/memory_engine/chroma_client.py
   ```
4. **Daily Usage:** Whenever you add new notes or documentation into the `memory-vault/` folder using an app like Obsidian, just re-run the `chroma_client.py` script. The agent will instantly understand everything you just wrote!

### 📱 Step 4: Connect the Agent to Telegram (Optional)
If you want to orchestrate your agent from your phone:

1. Open Telegram and search for `@BotFather`.
2. Send `/newbot`, give it a name, and copy the **Bot Token**.
3. In a terminal, set your variables and start the script:
   ```powershell
   # 1. Set your secret token (replace with the one from BotFather)
   $env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
   
   # 2. Set your User ID (so only YOU can command the bot)
   $env:TELEGRAM_AUTHORIZED_USERS="YOUR_TELEGRAM_ID_HERE"
   
   # 3. Install external packages
   pip install -r src/telegram_bot/requirements.txt
   
   # 4. Start the bot listener
   python src/telegram_bot/main.py
   ```
4. Open Telegram, start a chat with your new bot with `/start`, and try sending a command like `/exec echo "Hello World"`. The agent will tunnel this execution into the Docker sandbox instantly!

---

## Directory Structure
- `.agents/skills/` - Where the AI stores runbooks on how to use new tools.
- `.learnings/` - Persistent logs of errors and agent reflections.
- `docker/` - Holds the `Dockerfile.sandbox` for execution isolation.
- `memory-vault/` - Your Obsidian markdown directory.
- `scripts/` - Utilities for setting up WSL and patching IDEs to route to local models.
- `src/` - The Python source code for the ChromaDB memory and Telegram bot.

---
*Built based on "The Fully Open-Source Architecture for Always-On Local Agentic Systems: A Technical Blueprint."*
