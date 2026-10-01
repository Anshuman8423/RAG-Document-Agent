from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.rag import SimpleRAG


app = FastAPI(
    title="RAG Document Agent",
    description="Retrieval-Augmented Generation document question answering API",
    version="1.0.0",
)


rag_engine = SimpleRAG()


class DocumentRequest(BaseModel):
    documents: list[str] = Field(
        ...,
        min_length=1,
    )


class QueryRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
    )

    top_k: int = Field(
        default=3,
        ge=1,
        le=10,
    )


@app.get("/")
def root():

    return {
        "service": "rag-doc-agent",
        "status": "running",
    }


@app.get("/health")
def health():

    return {
        "service": "rag-doc-agent",
        "status": "healthy",
    }


@app.post("/documents")
def add_documents(request: DocumentRequest):

    rag_engine.add_documents(request.documents)

    return {
        "success": True,
        "document_count": len(
            rag_engine.documents
        ),
    }


@app.post("/query")
def query_documents(request: QueryRequest):

    if not rag_engine.documents:
        raise HTTPException(
            status_code=400,
            detail="No documents have been loaded",
        )

    results = rag_engine.search(
        request.question,
        request.top_k,
    )

    return {
        "success": True,
        "question": request.question,
        "results": results,
    }