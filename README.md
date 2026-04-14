# The Fully Open-Source Architecture for Always-On Local Agentic Systems: A Technical Blueprint

The transition toward agentic development signifies a shift from simple predictive completion to autonomous system orchestration. This architecture establishes a framework for a secure, local, and perpetually active agent-bot, utilizing Google Antigravity as the primary orchestration surface and Gemma 4 as the underlying cognitive engine. This approach prioritizes data sovereignty and verifiable autonomy, ensuring that sensitive developmental operations remain entirely within the user's local hardware infrastructure.

## 1. The Orchestration Surface: Google Antigravity as an Agent-First IDE

Google Antigravity represents a fundamental restructuring of the traditional developer interface, moving beyond the "chat-centric" models typical of early AI integrations. It is constructed as an agent-first platform, presupposing that the AI is not merely a tool for code generation but an autonomous actor capable of high-level planning, execution, and iterative validation.

### Operational Modes and Artifact Verifiability

Trust in autonomous systems is established through transparency. Antigravity addresses this through a system of artifacts—intermediate deliverables that allow for human review without constant interruption. These artifacts include Task Lists, which break down prompts into actionable sequences, and Implementation Plans, which serve as architectural roadmaps that the user must approve.

The system operates in two primary modes:
*   **Planning Mode**: Utilized for deep research and complex architectural changes, producing comprehensive artifacts.
*   **Fast Mode**: Optimized for localized, lower-risk tasks such as variable renaming or simple terminal commands.

| Feature | Description | Operational Impact |
| :--- | :--- | :--- |
| **Agent Manager** | Surface for orchestrating multiple asynchronous agents. | Multiplies developer throughput through parallel task execution. |
| **Artifact System** | Generates Task Lists and Implementation Plans. | Enables high-level validation of AI "thought processes". |
| **Mission Control** | High-level orchestration surface. | Centralizes monitoring for specialized AI agents. |
| **Browser Subagent** | Headless browser for web navigation and UI testing. | Allows agents to verify their own work on localhost. |

## 2. The Cognitive Engine: Gemma 4 Neural Architecture (The "Brain")

The Gemma 4 model family is the designated "brain" for this architecture, specifically optimized for agentic workflows, complex reasoning, and multimodal understanding.

### Neural Architecture and the "Precision Trap"

A critical technical nuance of the Gemma 4 architecture is its departure from standard transformer scaling. Gemma 4 employs a specific normalization scheme making the model approximately 22 times more sensitive to numerical precision errors compared to standard transformers like Llama.

For local deployment, this sensitivity introduces a "precision trap" regarding Key-Value (KV) cache management. Analysis indicates that using an F16 KV cache with a BF16 model leads to compounded precision loss across decode steps, often resulting in output degeneration after approximately 50 tokens. Stable execution requires strict adherence to data type consistency: BF16 models should ideally utilize a BF16 KV cache with F32 internal attention math to ensure accuracy.

| Model Variant | Architecture Type | Recommended RAM | Key Advantage |
| :--- | :--- | :--- | :--- |
| **Gemma 4 31B** | Dense | 35 GB | Maximum reasoning and complex task planning. |
| **Gemma 4 26B-A4B** | Mixture of Experts (MoE) | 16 GB - 30 GB | Optimal speed; activates only 3.8B - 4B parameters per pass. |
| **Gemma 4 E4B** | Small Dense | 6 GB | Capable of repository audits on mobile/laptop. |
| **Gemma 4 E2B** | Ultra-Small Dense | 4 GB - 5 GB | Efficient for Raspberry Pi or basic automation. |

Local serving is facilitated through **Ollama** or **LM Studio**, which provide OpenAI-compatible endpoints. For environments with large system prompts (8,000+ tokens), LM Studio is often preferred as it may offer superior default prefix caching, preventing repetitive re-processing of static instructions.

## 3. The Pre-Frontal Cortex: Orchestration with OpenClaw and Plandex

The orchestrator manages the "agent loop"—the infrastructure required for persistent identity, memory, and task continuity.

### OpenClaw and Agent Identity

OpenClaw differentiates itself by focusing on agent identity and self-improvement. Central to its architecture is the `SOUL.md` file, which defines the agent’s personality and long-term goals, creating a framework for "artificial continuity". Every agent functions within an isolated directory (`agentDir`) that contains its own configuration and skill definitions, ensuring sensitive data does not leak between specialized agents.

### Task Planning and Asynchronous Execution

For complex engineering, **Plandex** provides a terminal-based alternative focused on deep architectural changes, breaking requests into subtasks and delegating them to worker agents. While OpenClaw excels at messaging-integrated automation, Plandex is optimized for intensive development work within a local repository.

## 4. Memory Architecture: Long-Term Storage with Obsidian and ChromaDB

A sophisticated agent requires a compounding memory system that distinguishes between ephemeral session data and durable project knowledge. This blueprint implements a three-layer memory strategy.

### The Three-Layer Memory Model

1.  **Working Memory (Layer 1)**: Raw session logs capturing interactions in real-time.
2.  **Curated Memory (Layer 2)**: Distilled logs where the agent identifies key decisions and successful strategies via a periodic "reflection" cycle.
3.  **Structured Vault (Layer 3)**: Implemented as a local Obsidian repository, containing permanent documentation and strategic guides.

### Vector Retrieval via ChromaDB

**ChromaDB** serves as the engine for semantic search. Text is converted into numerical embeddings and indexed along with metadata (timestamps, user identifiers). When a query is received, the system performs a similarity search (e.g., cosine similarity) to retrieve the most relevant entries, injecting them into the LLM prompt to enable the agent to "remember" context from months prior.

## 5. Secure Execution: Sandboxing with Docker, WSL2, and PowerShell

Granting an AI agent system-level access necessitates a "secure-by-design" environment. This architecture leverages Docker Desktop and WSL2 to create isolated boundaries.

### The Docker-WSL2 Security Boundary

To make autonomous operations safe, every agentic action is contained within a disposable Docker Sandbox, often based on MicroVM technology. WSL2 provides the Linux kernel required for Docker to operate efficiently on Windows, while "mirrored networking" ensures the agent can be managed from both Windows PowerShell and the Linux guest.

PowerShell serves as the "hands," providing the interface to manage the Windows laptop and the WSL2 environment. Scripts can automate the installation and configuration of these components to ensure the system remains "always-on" and ready to respond.

## 6. Remote Communication: Telegram and the Proton Mail Bridge

The interface layer provides secure remote interaction while preserving end-to-end encryption.

### Telegram Remote Control

Using the `python-telegram-bot` library, the agent is connected to a Telegram channel. Access control is enforced through a whitelist of numeric User IDs, ensuring only the authorized owner can trigger sensitive commands like `/exec`.

### Private Email Tunneling

For interactions requiring email, Proton Mail Bridge creates a secure local server. The agent interacts with this bridge via standard SMTP (port 1025) and IMAP (port 1143) protocols using specific bridge-generated credentials. This ensures all email traffic is encrypted before leaving the machine.

## 7. The Self-Learning Loop: Skill Distillation

The final layer is the self-learning mechanism, allowing the agent to evolve based on experience.

### Error Logging and Insights

The agent maintains a `.learnings/` directory to capture unexpected operation failures, user corrections, and insights. An Extraction Workflow analyzes these logs; if an error is recurring, the agent distills the solution into a concise rule and adds it to the workspace memory (e.g., `AGENTS.md`).

### The Skills Folder and SKILL.md Standard

Skills are an open standard for extending capabilities, consisting of a directory with a `SKILL.md` file containing instructions and best practices. When the agent discovers a non-obvious solution, it can autonomously create a new skill in `.agents/skills/`. By synchronizing these folders with GitHub, the agent's progress is version-controlled and resilient to data loss.

## 8. Technical Implementation: Patching Antigravity for Local Models

While Google Antigravity prioritizes cloud models, it can be patched to support local models via Ollama. This is achieved by modifying the shipped JavaScript bundles (`workbench.desktop.main.js` and `jetskiAgent/main.js`) to remove "googleInternal" gates.

| Configuration Field | Local Value | Purpose |
| :--- | :--- | :--- |
| `requestedModel` | `GOOGLE_GEMINI_INTERNAL_BYOM` | Satisfies language server allowlist. |
| `apiProvider` | `API_PROVIDER_OPENAI_VERTEX` | Routes to OpenAI-compatible adapter. |
| `baseUrl` | `http://localhost:11434/v1` | Redirects requests to local Ollama. |
| `modelName` | `<ollama_tag>` | Specifies the local model version to load (e.g., `gemma4:31b`). |
