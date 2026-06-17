# llm-zoomcamp-2026-code
<img width="1769" height="889" alt="llm-zoomcamp-2026" src="https://github.com/user-attachments/assets/d6f8d2ec-825d-4450-ba1e-11811962822c" />

# 🚀 LLM Zoomcamp 2026 Journey

Welcome to my personal hands-on repository documentation tracking my progress through the **[DataTalksClub LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)**, an intensive 10-week program led by **[Alexey Grigorev](https://github.com/alexeygrigorev)** focused on building production-grade LLM applications and Retrieval-Augmented Generation (RAG) systems.

This repository serves as a live ledger of my engineering implementations, core architectural experiments, homework deliverables, and system monitoring setups.

---

## 🛠️ Technology Stack & Orchestration

Throughout this curriculum, I transition from foundational mathematical concepts to fully deployed full-stack pipelines using these technologies:

⚡ **Languages & Environments:** ![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast%20Package%20Manager-DE5C2E?style=flat-square)

🧠 **LLMs & Frameworks:**
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat-square&logo=openai&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-API-F5511E?style=flat-square)
![ToyAIKit](https://img.shields.io/badge/Framework-ToyAIKit-blueviolet?style=flat-square)

🗄️ **Vector Storage & Infrastructure:**
![Kestra](https://img.shields.io/badge/Orchestration-Kestra-2F1B4E?style=flat-square&logo=kestra)
![Grafana](https://img.shields.io/badge/Monitoring-Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)
![SQLite](https://img.shields.io/badge/Storage-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

---

## 📅 Curriculum Tracker & Repository Mapping

Below is the directory map linking to my distinct technical implementations and completed module milestones:

| Week / Chapter | Focus Area & Key Milestones | Core Tech Used | Code / Artifact Links |
| :--- | :--- | :--- | :--- |
| **01. Agentic RAG** | Document ingestion, text chunking parsing, manual function-calling evaluation loops, and autonomous agent tracking using minimalistic frameworks. | Python, OpenAI SDK, Groq API, ToyAIKit | [`/1-Agentic_Rag`](./1-Agentic_Rag/) |
| **02. Open-Source LLMs** | Running local model runtimes, quantization mechanics, context window boundaries, and prompt formatting pipelines. | Ollama, Hugging Face | *[Coming Soon]* |
| **03. Vector Search** | Embedding generation, metric spaces (Cosine/L2 similarity), index scaling, and retrieval hyperparameter fine-tuning. | Elasticsearch / Qdrant | *[Coming Soon]* |
| **04. Orchestration** | Developing automated document processing pipelines, data synchronization, and pipeline scheduling systems. | Kestra, Postgres | *[Coming Soon]* |
| **05. Evaluation** | RAG evaluation mechanics, RAGAS frameworks, generation metrics (faithfulness, answer relevance), and automated testing suites. | Python, LLM-as-a-Judge | *[Coming Soon]* |
| **06. Monitoring** | Production logging, tracking drift, monitoring latency, user feedback loops, and live dashboards. | Grafana, Prometheus | *[Coming Soon]* |

---

## ⚙️ Environment Setup & Local Development

This project relies on **`uv`** as its lightning-fast package manager and environment isolated workspace runner. Follow these instructions to spin up the local environment:

### 1. Clone the Workspace
git clone
https://github.com/Latrechesara/llm-zoomcamp-2026-code

cd llm-zoomcamp-2026-code

2. Initialize Virtual Environment and Dependencies
# Sync lockfile configurations and build the environment automatically
uv sync

3. Key Credentials Configuration
Create a .env file within your active working directory or target module subfolder (1-Agentic_Rag/):
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here

🎓 Acknowledgments
Original Course Repository: [DataTalksClub/llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)

Course Founder: Alexey Grigorev

Using uv, you don't need to manually create environments or activate raw pip setups. Run:
