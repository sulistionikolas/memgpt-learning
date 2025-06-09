# 🧠 memgpt-learning

An experimental project inspired by [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560), aimed at understanding memory management in Large Language Models. This project is designed for local experimentation and potential alignment with memory-intensive fintech use cases.

---

## 🎯 Objectives

- Explore the memory architecture of MemGPT
- Recreate simplified MemGPT-like memory paging using local tools
- Gain hands-on experience in:
  - LLM integration (initially API-based, later self-hosted)
  - Context window management and eviction strategies
  - Local vector DB and persistent memory handling
  - Python (DS, AI engineering, and DevOps basics)

---

## 🛠️ Tech Stack (Planned)

| Layer              | Current (Phase 1)                     | Future (Phase 2)                 |
|-------------------|----------------------------------------|----------------------------------|
| LLM Engine         | Hugging Face API: Mistral-7B          | Self-hosted Mistral/LLaMA (via `llama.cpp` or `vLLM`) |
| Embeddings         | HF Transformers / OpenAPI             | Locally hosted embedding models  |
| Vector Database    | In-memory / mock                      | Qdrant / pgvector                |
| Storage            | Python dicts / flat files             | PostgreSQL (archival/recall tiers) |
| Interface          | `.ipynb` notebook (VSCode)            | Modular `.py` files + CLI/FastAPI |

---

## 📁 Project Structure (In Progress)