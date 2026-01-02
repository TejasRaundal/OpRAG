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

- **Frontend:** Tauri (desktop UI) Svelte + Vite + TypeScript
- **Backend API:** FastAPI (Using LangChain code for Text Splitters, Prompt Templates, Document Loaders, Retrieval ALgos, Agents)
- **Model runtime / Embeddings:** ONNX (local model inference for embeddings) all-MiniLM-L6-v2
- **Vector database:** Qdrant (on‑premise vector search)
- **Relational DB:** PostgreSQL (for metadata, users, and configs)
- **Software Design Pattern:** Hexagonal Architecture (Ports and Adapters)

## Quick Start — UI (development)

**Prerequisites:** Node.js + npm, Rust & cargo, Python (for mock API). For full stack testing also have Qdrant and PostgreSQL running locally.

1. Install JS deps: `npm install`
2. Start mock backend (dev): `uvicorn mock.mock_api:app --reload --port 8000`
3. Start frontend dev server: `npm run dev` (visit http://localhost:5173)
4. To run full desktop app during development: `npm run tauri:dev`
5. To build a production binary: `npm run tauri:build`

**Notes:**
- Follow the Hexagonal Architecture: keep adapters (API calls) in `src/lib` (ports/adapters), UI components in `src/components`, and domain logic in `src/services`.
- Use TypeScript and small, testable functions; persist user config via Tauri APIs when ready.
