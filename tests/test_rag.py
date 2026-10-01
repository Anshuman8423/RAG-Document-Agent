from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["service"] == "rag-doc-agent"


def test_health():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_query_without_documents():

    response = client.post(
        "/query",
        json={
            "question": "What is Python?",
            "top_k": 3,
        },
    )

    assert response.status_code == 400


def test_add_documents():

    response = client.post(
        "/documents",
        json={
            "documents": [
                "Python is a programming language.",
                "FastAPI is a Python web framework.",
                "RAG systems retrieve relevant documents."
            ]
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["document_count"] == 3


def test_query_documents():

    response = client.post(
        "/query",
        json={
            "question": "Python programming language",
            "top_k": 2,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert len(data["results"]) > 0