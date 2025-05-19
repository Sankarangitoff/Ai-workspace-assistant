# AI Workspace Assistant

A modern, AI-powered productivity web application that brings together intelligent document interaction and goal-oriented task planning. This assistant combines natural language understanding with advanced memory and planning capabilities to enhance personal and team productivity.

---

## 🚀 Overview

**AI Workspace Assistant** is a unified assistant designed to help users:

* Upload and query documents using natural language.
* Extract summaries, action items, and FAQ-style responses.
* Break down high-level goals into structured, actionable tasks.
* Retain memory of interactions to improve context and usability over time.

---

## 🎯 Key Features

| Feature                         | Description                                                         |
| ------------------------------- | ------------------------------------------------------------------- |
| 📄 Multi-File Upload            | Upload PDFs, CSVs, plain text, or Docs                              |
| 💬 Natural Language Q\&A        | Ask questions and receive cited answers from uploaded content       |
| 📑 Summarization & Action Items | Extract key summaries and decisions from docs and meeting notes     |
| 🧠 Goal Planner                 | Turn high-level goals into subtasks with intelligent agent support  |
| 🧭 Smart File Routing           | Automatically identify and route documents by type (PDF, CSV, etc.) |
| 🗂️ Vector Memory               | Store past conversations and preferences for smarter context        |
| 📈 Feedback Logging             | Enable feedback to improve AI responses over time                   |

---

## 🧠 Tech Stack

| Layer         | Technology                                       |
| ------------- | ------------------------------------------------ |
| LLM           | Gemini 1.5                                       |
| Orchestration | LangChain (Agents, Chains, Memory)               |
| Backend       | FastAPI                                          |
| Vector Store  | ChromaDB                                         |
| Loaders       | LangChain Document Loaders (PDF, CSV, Docs, TXT) |

---

## 💡 Use Cases

* Retrieve internal knowledge from policies and product documentation
* Summarize meeting notes and create follow-up tasks
* Q\&A over legal documents and contracts
* Goal setting and automatic task breakdown
* Analyze and ask questions on CSV reports

---

## 🔮 Future Scope

* Fine-tuning models for legal, HR, and marketing domains
* Web-based UI with real-time conversational memory
* Multi-user support with individual histories and access

---

## Project Structure

- `app/`: Contains the main application code
- `data/`: Data storage directory
- `db/`: Database related files
- `main.py`: Main entry point of the application

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main application:
```bash
python main.py

## 🛠️ Getting Started

### Step 1: Clone the Repository

```bash
git clone <repo-url>
cd Ai_workspace_assistant
```

### Step 2: Setup Virtual Environment

```bash
python -m venv venv
./venv/Scripts/Activate.ps1  # Windows PowerShell
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install fastapi uvicorn langchain openai chromadb python-dotenv \
            google-generativeai sentence-transformers pypdf \
            python-docx unstructured python-doc python-multipart \
            pandas tabulate openpyxl passlib[bcrypt] \
            fastapi[all] python-jose[cryptography]
```

### Step 4: Run the Server

```bash
uvicorn main:app --reload
```
Add gemini key in .env file
---

## 📁 File Structure

* `main.py` – Main FastAPI app
* `app/` – Frontend static files (HTML, CSS, JS)

  * `index.html` – Login & registration
  * `dashboard.html` – Chat & file management
  * `planner.html` – Task planner UI
* `assets/` – Images and logos
* `styles.css`, `custom.css`, etc. – Stylesheets
* `planner.js`, `app.js` – JS logic


---

## 🤝 Contributing

Pull requests are welcome! For significant changes, please open an issue to discuss your ideas first.

---

## 📄 License

[MIT](LICENSE)

---

**AI Workspace Assistant – Smarter Work, Simpler Life.**
