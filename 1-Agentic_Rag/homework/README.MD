# 📔 Module 1 Homework: Agentic RAG

This folder contains my solutions and engineering implementations for the Module 1 Homework of the LLM Zoomcamp. The core focus of this assignment was moving from standard linear Retrieval-Augmented Generation (RAG) to an autonomous, self-correcting agentic loop using tool-calling.

## 👥 Homework Deliverables

* **`1-Agentic_rag_homework_Homework.ipynb`**: The primary Jupyter Notebook containing the full execution, token tracking, and final evaluation loops.
* **`rag_helper_hw.py`**: A modularized helper script containing custom parsing mechanics, chunking configurations, and retrieval functions used to support the notebook.

---

##  Key Implementations & Concepts Covered

### 1. Document Indexing & Retrieval
* Implemented a local search index over the course text chunks.
* Designed the `search` utility function with precise type hinting and descriptive docstrings, allowing modern LLM frameworks to dynamically generate JSON tool schemas via introspection.

### 2. Manual vs. Framework-Driven Agentic Loops
* **Handwritten Loop**: Built an explicit `while True` loop to manage the state machine, parsing tool calls from the assistant response, executing the local index lookup, and feeding outputs back into conversation history.
* **Framework Integration**: Abstracted the boilerplate logic using **`toyaikit`**, leveraging its `Tools` registry and `OpenAIResponsesRunner` to evaluate multi-turn behaviors with less code.

### 3. Agentic Behavior Analysis
* **The Assignment Target (Q6)**: Prompted the model to analyze how an agentic loop operates differently from a single-shot RAG pipeline.
* **Instruction Nudging**: Observed how strict system prompts force the model to recursively look up content chunks multiple times (averaging **4 tool executions** with `gpt-4o-mini`) rather than answering immediately from pre-trained parametric memory.

---

##  How to Run This Module

Make sure your root environment is properly configured via `uv` or your active virtual environment, then ensure your keys are set in this folder's `.env`:

```env
OPENAI_API_KEY=your_key_here
