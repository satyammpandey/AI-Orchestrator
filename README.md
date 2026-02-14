# 🪐 AI-Orchestrator
### Autonomous Multi-Agent Intelligence System

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Version-2.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-Next.js-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Groq%20LLaMA-orange?style=for-the-badge" />
</p>

---

## 🚀 Overview

AI-Orchestrator is a full-stack, agentic AI execution system that coordinates multiple specialized AI agents to transform complex user directives into structured, research-backed, and technically validated outputs.

It demonstrates real-world multi-agent orchestration, RAG pipelines, OCR integration, and modular AI system design.

---

# 🤖 The AI Agent Workforce

| Agent | Role |
|-------|------|
| 🎯 **Orchestrator** | Breaks down user goals into structured execution plans |
| 🔍 **Researcher** | Performs live web research + PDF/OCR extraction |
| 📊 **Analyst** | Applies reasoning, pattern detection, structured evaluation |
| 💻 **Coder** | Generates code, debugging logic, architecture designs |
| ✍️ **Writer** | Synthesizes final structured intelligence report |

All agents operate through a mission-based execution pipeline inside a FastAPI backend.

---

# 🧠 Architecture

```
           ┌────────────────────┐
           │  Next.js Frontend  │
           └─────────┬──────────┘
                     │
                     ▼
           ┌────────────────────┐
           │   FastAPI Backend  │
           └─────────┬──────────┘
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
  SQLite DB     Vector Store     Groq LLaMA
  (Auth/Data)    (RAG Memory)     (LLM Engine)
```

---

# ⚡ Core Capabilities

## 🔹 Intelligence & Workflow
- Multi-Agent Autonomous Execution
- Structured Task Decomposition
- RAG-based File Understanding
- Multi-phase Project Reasoning
- Contextual Memory Handling

## 🔹 Document & Research Engine
- PDF Parsing (PyMuPDF)
- Handwriting OCR (Tesseract)
- Live Web Research (DuckDuckGo Integration)

## 🔹 Real-Time Interaction
- Direct Agent Terminal Mode
- Smart Code Block Rendering
- Mission Status Feedback System

## 🔹 Authentication & Security
- Login / Registration System
- Session-based Authentication
- Protected API Routes

---

# 🛠 Tech Stack

### Backend
- Python 3.10+
- FastAPI
- Uvicorn
- SQLite
- PyMuPDF
- Tesseract OCR

### Frontend
- Next.js 14
- Tailwind CSS
- React-Hot-Toast

### AI Layer
- Groq LLaMA 3.3-70B
- RAG-based Context Injection

---

# 📂 Project Structure

```
AI-Orchestrator/
│
├── backend/
│   ├── agents/
│   ├── api/
│   ├── memory/
│   ├── tools/
│   └── main.py
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── services/
│
└── run.bat
```

---

# 🚀 Quick Start

## 1️⃣ Clone Repository

```bash
git clone https://github.com/satyammpandey/AI-Orchestrator.git
cd AI-Orchestrator
```

---

## 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Backend runs on:
```
http://localhost:8001
```

---

## 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:
```
http://localhost:3000
```

---

# 📡 API Endpoints

| Endpoint | Description |
|-----------|------------|
| `/api/tasks` | Multi-agent execution pipeline |
| `/api/auth` | Authentication routes |

---

# 🗺 Roadmap

- [x] Multi-Agent Core Architecture
- [x] PDF + OCR Intelligence
- [x] Direct Agent Mode
- [ ] Report Export (PDF / Markdown)
- [ ] Docker Deployment
- [ ] Cloud Hosting

---

# ⚖ License

MIT License

---

# 👨‍💻 Author

**Satyam Pandey**  

