# Agentic AI Workflow Assistant

An agentic Large Language Model (LLM) assistant that autonomously performs multi-step tasks (like “Book my flight + hotel + calendar block”) by orchestrating API tool calls using [LangGraph](https://langgraph.org/).

---

## ✈️ What does it do?

Given a high-level natural language instruction, the assistant:
1. **Parses the task** (e.g., "Book my flight from NYC to SFO Aug 10-15, get me a hotel, block calendar")
2. **Decomposes steps**: flight booking → hotel reservation → calendar event
3. **Orchestrates APIs** through a workflow graph with memory & dependencies
4. **Confirms results** with the user

---

## 🏗️ Architecture

```
User Request
   │
   ▼
LLM Agent (LangGraph)
   │
   ├─> Tool/Function Selection (Flight, Hotel, Calendar APIs)
   │      │
   │      └─> API Execution
   │
   └─> Step Execution Graph (Multi-Step Planning)
   │
   ▼
Response/Confirmation to User
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Ahmad-Khalil-LEEA/agentic-ai-workflow-assistant.git
cd agentic-ai-workflow-assistant
```

### 2. Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure API Keys

- Rename `.env.example` to `.env`
- Fill in your API keys for flight, hotel, and calendar services

### 4. Run the assistant

```bash
python agentic_assistant.py
```

---

## 🧩 Code Structure

- `agentic_assistant.py` — Main workflow agent using LangGraph
- `tools/` — API tool wrappers: `flight.py`, `hotel.py`, `calendar.py`
- `.env.example` — Environment variable example
- `requirements.txt` — Python dependencies

---

## 📝 Example Usage

**User:**  
Book my flight from NYC to San Francisco Aug 10-15, get me a hotel near Moscone Center, and block it in my calendar.

**Assistant:**  
- Books flight & hotel via API
- Blocks calendar event
- Returns summary & confirmation

---

## 🛠️ Extending

- Add more tools (e.g., rideshare, events)
- Add conversational clarifications for ambiguous info
- Multi-user/group planning

---

## 📄 License

MIT License
