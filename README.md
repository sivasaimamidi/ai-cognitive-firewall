---
title: AI Cognitive Firewall
emoji: 🛡️
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---
# 🛡️ AI Cognitive Firewall

An enterprise-grade, real-time threat detection and mitigation layer designed to secure Agentic AI systems. Built for the Meta Hackathon.

## 📖 Overview
The **AI Cognitive Firewall** acts as an autonomous security layer intercepting LLM actions, evaluating agentic inputs and tool executions across different operational layers (Presentation, Tool, Memory, Authorization, and Execution). It ensures AI agents do not leak data, accept poisoned memory fragments, or execute malicious instructions like reverse shells.

## ✨ Features
We evaluate the firewall against 5 critical enterprise threat vectors:
1. **Direct Prompt Injection** - Refuses adversarial instructions trying to extract the system prompt.
2. **Semantic Tool Output Compromise** - Distrusts manipulated database outputs injecting malicious downstream instructions.
3. **Goal Hijacking via Memory Poisoning** - Detects and prevents poisoned memory fragments (Simulated Pinecone RAG) from rewriting safe instructions (e.g., inserting phishing links).
4. **RBAC Privilege Escalation** - Blocks unauthorized attempts to elevate user roles.
5. **Reverse Shell Injection** - Identifies and blocks critical RCE proxy payloads.

Also includes an **Interactive Real-Time HTML Dashboard** connected natively to our local FastAPI evaluation environment!

## 🚀 Tech Stack
- **Backend Environment:** Python, FastAPI, simulated OpenEnv state architecture.
- **LLM Integration:** Groq Superfast Inference Engine (`llama-3.1-8b-instant`).
- **Memory Logic:** Simulated Pinecone Vector DB RAG endpoints.
- **Frontend Panel:** TailwindCSS + Vanilla JS Web Dashboard.

## 🛠️ Setup & Installation

### 1. Requirements
- Python 3.11+
- A valid [Groq API Key](https://console.groq.com)

### 2. Environment Variables
Ensure you have a `.env` file in the root folder that looks like this:
```env
HF_TOKEN=gsk_your_groq_api_key_here
API_BASE_URL=http://localhost:8000
MODEL_NAME=llama-3.1-8b-instant
MODEL_SERVER_URL=https://api.groq.com/openai/v1
```

### 3. Install
```bash
pip install -r requirements.txt
```

## 🎮 How to Run

**1. Start the Evaluation Environment Server (Background)**
```bash
python -m server.app
```
*(Leave this running in the background).*

**2. Launch the Dashboard**
Simply double-click `dashboard.html` in your file explorer. It will open natively in your browser and will securely bridge to your local backend to visualize the threat responses manually.

**3. Run the LLM Firewall Engine**
Open a new terminal window in the project folder and run:
```bash
python inference.py
```
*You can also run specific tasks by adding an argument: `python inference.py task_1`*

## 🧪 Testing the Grading Logic
We have a local testing suite built out to verify the task boundaries of the firewall graders rapidly without needing external LLM API calls.
```bash
python test_logic.py
```
