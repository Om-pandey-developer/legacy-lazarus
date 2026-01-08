# 🏛️ Legacy Lazarus: Autonomous Code Migration Agent

> **"Don't just translate code. Reincarnate behavior."**

![Gemini](https://img.shields.io/badge/AI-Google%20Gemini%201.5-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white)
![Python](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 💡 The Problem
The world's critical infrastructure runs on "Black Box" legacy code. Migrating it is high-risk because documentation is missing and hidden logic (like undocumented bonuses or edge cases) is easily lost during translation.

**Legacy Lazarus** is an autonomous agent that solves this by **validating behavior, not just syntax.** It uses a **Self-Healing Loop** to ensure the modern code produces identical outputs to the legacy code, mathematically guaranteeing 100% parity.

---

## 🧠 System Architecture

Legacy Lazarus treats legacy migration as a **scientific experiment**: observe the old, hypothesize the new, test, and correct.

```mermaid
graph TD
    subgraph "Phase 1: Behavioral Analysis"
    A[Legacy Code Input] -->|Static Analysis| B(Generate Truth Table)
    B -->|Input Vectors| C[Legacy Execution Sandbox]
    C -->|Outputs| D[Behavioral Profile]
    end

    subgraph "Phase 2: Agentic Refactoring"
    D --> E{Gemini Agent}
    E -->|Generate Code| F[Modern Sandbox]
    F -->|Run Test Vectors| G[Mirror Test Verification]
    end

    subgraph "Phase 3: Self-Healing Loop"
    G -- "MISMATCH" --> H[Error Analysis Module]
    H -->|Inject Error Context + Hints| E
    G -- "PARITY ACHIEVED" --> I[✅ Final Output]
    end
    
    style E fill:#4285F4,stroke:#333,stroke-width:2px,color:white
    style H fill:#EA4335,stroke:#333,stroke-width:2px,color:white
    style I fill:#34A853,stroke:#333,stroke-width:2px,color:white

    🚀 Key Features
1. 🛡️ Behavioral Truth Tables
Instead of guessing, the agent runs the legacy code in a secure sandbox with various input vectors (edge cases, typical values) to record exactly how it behaves.

2. 🔄 Self-Healing "Mirror Test"
The system runs the new code against the same inputs.

If it matches: The code is approved.

If it fails: The agent captures the error (e.g., Mismatch at 40 hours), analyzes the logs, and rewrites the code automatically.

3. 📉 Complexity Reduction
We use Radon analysis to quantify technical debt. The dashboard validates that the new code isn't just correct, but cleaner (e.g., reducing Cyclomatic Complexity from 13 to 3).

🛠️ Tech Stack
AI Model: Google Gemini API (via google-generativeai)

Backend: Python FastAPI, Uvicorn, Subprocess (Sandboxing)

Analysis: Radon (Cyclomatic Complexity Metrics)

Frontend: React (Vite) with Terminal-style UI

Security: python-dotenv for secure key management

💿 Installation & Setup
Prerequisites
Node.js & npm
Python 3.9+
Google Gemini API Key
1. Clone the Repository
Bash

git clone https://github.com/YOUR_USERNAME/legacy-lazarus.git
cd legacy-lazarus
2. Backend Setup
Bash

cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
Configuration: Create a .env file in the backend folder:

Code snippet

GEMINI_API_KEY=your_actual_api_key_here
3. Frontend Setup
Open a new terminal:

Bash

cd frontend
npm install
⚡ Usage
Start the Backend Server:

Bash

# Inside /backend
python -m uvicorn main:app --reload
Start the Frontend Interface:

Bash

# Inside /frontend
npm run dev
Run the Agent:

Open http://localhost:5173

Click ACTIVATE LAZARUS AGENT

Watch the terminal logs as the agent ingests code, detects errors, and self-corrects in real-time.

🏆 Hackathon Context
This project was built for the Google Gemini "Action Era" Hackathon.

Most AI coding tools are "Assists"—they help you type. Legacy Lazarus is an Agent—it does the job for you. By combining Gemini's reasoning capabilities with a robust execution feedback loop, we bridge the gap between "Generative Text" and "Reliable Engineering."

📜 License
Distributed under the MIT License. See LICENSE for more information.