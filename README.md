# OpRAG — On‑Premise Offline RAG for Indian Businesses 🎯

**OpRAG** (On‑Premise Retrieval‑Augmented Generation) is a compact desktop application designed to provide secure, offline RAG capabilities for Indian businesses and industries. It prioritizes data privacy, on‑site control, and practical value for organizations that prefer or require on‑premise solutions.

---

## Overview

- On‑premise, offline RAG desktop application that keeps sensitive business data local. 🔒
- Built to serve Indian SMEs, manufacturing, healthcare, legal, government, and other industry sectors. ✅

## Why OpRAG?

- **Data privacy & compliance:** Keeps data on‑site to help meet regulatory and confidentiality needs.
- **Offline‑first:** Works where internet connectivity is limited or intermittent.
- **Industry focus:** Tailors knowledge bases and retrieval strategies to domain‑specific workflows.
- **Local language support:** Prioritizes Indian languages and formats. 💡

## Key Features (high level)

- Secure on‑premise knowledge ingestion and indexing
- Offline retrieval and generative responses using local resources
- Configurable knowledge bases for industry workflows
- Simple UI for business users and administrators

## Tech Stack

- **Frontend:** Tauri (desktop UI)
- **Backend API:** FastAPI
- **Model runtime / Embeddings:** ONNX (local model inference for embeddings)
- **Vector database:** Qdrant (on‑premise vector search)
- **Relational DB:** PostgreSQL (for metadata, users, and configs)
