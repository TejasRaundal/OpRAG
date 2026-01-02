from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class TextPayload(BaseModel):
    text: str

class QueryPayload(BaseModel):
    query: str

@app.post('/embed')
async def embed(payload: TextPayload):
    # return a dummy fixed-dim vector (e.g., 384 dims) for dev
    vec = [random.random() for _ in range(384)]
    return {"vector": vec}

@app.post('/search')
async def search(payload: QueryPayload):
    # return dummy search results
    return {"results": [{"id": "doc1", "score": 0.92, "text": "This is a matched doc (mock)"}]}

@app.post('/index')
async def index(docs: dict):
    return {"status": "ok", "indexed": len(docs.get('docs', []))}

# Run: uvicorn mock.mock_api:app --reload --port 8000