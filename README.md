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

   