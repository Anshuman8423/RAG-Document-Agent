# RAG Document Agent

An AI-powered document question-answering system built using **Retrieval-Augmented Generation (RAG)**. The project allows users to provide documents and ask questions about their content, while the system retrieves relevant information before generating an answer using an LLM.

## 🚀 Features

- 📄 **Document Upload**
  - Upload and process documents for AI-powered question answering.

- 🔍 **Semantic Search**
  - Finds relevant document content based on the meaning of the user's query.

- 🤖 **LLM-Powered Answers**
  - Uses a Large Language Model to generate natural-language answers.

- 🧠 **Retrieval-Augmented Generation**
  - Combines document retrieval with LLM generation.
  - Helps ground responses in the provided documents.

- 💬 **Question Answering**
  - Ask natural-language questions about uploaded documents.

- 📚 **Context-Aware Responses**
  - Retrieves relevant chunks of information and provides them as context to the LLM.

- ⚡ **Scalable Architecture**
  - The system can be extended to support multiple documents, users, and vector databases.

---

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** is an architecture that combines information retrieval with Large Language Models.

Instead of asking an LLM to answer a question only from its internal knowledge, RAG first searches a knowledge source and then provides the relevant information to the LLM.

```text
User Question
      │
      ▼
Query Processing
      │
      ▼
Vector Search
      │
      ▼
Relevant Document Chunks
      │
      ▼
Context + Question
      │
      ▼
      LLM
      │
      ▼
Generated Answer
```

---

## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Query API     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Query Embedding │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Vector Database │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Relevant Chunks │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      LLM        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Answer      │
                    └─────────────────┘
```

---

## 📄 Document Processing Pipeline

When a document is uploaded, it goes through several stages:

```text
Document
   │
   ▼
Text Extraction
   │
   ▼
Text Cleaning
   │
   ▼
Chunking
   │
   ▼
Embedding Generation
   │
   ▼
Vector Database
```

### Query Pipeline

```text
User Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build Context
      │
      ▼
LLM
      │
      ▼
Final Answer
```

---

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** FastAPI
- **LLM:** Large Language Model API
- **Embeddings:** Embedding Model
- **Vector Database:** Vector Store
- **Document Processing:** Document/Text Processing Libraries
- **API:** REST
- **Environment Management:** `.env`
- **Version Control:** Git & GitHub

> The exact LLM, embedding model, and vector database can be configured according to the project implementation.

---

## 📁 Project Structure

```text
rag-doc-agent/
│
├── app/
│   ├── api/
│   │   ├── ...
│   │
│   ├── ingestion/
│   │   ├── ...
│   │
│   ├── retrieval/
│   │   ├── ...
│   │
│   ├── llm/
│   │   ├── ...
│   │
│   └── main.py
│
├── documents/
│   └── ...
│
├── tests/
│   └── ...
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd rag-doc-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
LLM_API_KEY=your_api_key_here
EMBEDDING_API_KEY=your_embedding_api_key_here
VECTOR_DATABASE_URL=your_vector_database_url
```

Configure the variables according to the services used by the project.

### ⚠️ Important

Never commit API keys or secrets to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

If Swagger documentation is enabled, open:

```text
http://127.0.0.1:8000/docs
```

---

## 📤 Document Ingestion

The document ingestion process converts documents into searchable vector representations.

```text
              Document
                  │
                  ▼
          Extract Text
                  │
                  ▼
             Split Text
                  │
                  ▼
        Create Embeddings
                  │
                  ▼
          Store Vectors
                  │
                  ▼
         Vector Database
```

Each document is divided into smaller chunks so that relevant information can be efficiently retrieved during question answering.

---

## 💬 Example Query

A user can ask:

```text
What are the main objectives mentioned in the document?
```

The system then:

1. Converts the question into an embedding.
2. Searches the vector database.
3. Retrieves the most relevant document chunks.
4. Adds those chunks to the LLM context.
5. Generates the final answer.

---

## 🔌 Example API

### Upload Document

```http
POST /documents/upload
```

Example:

```bash
curl -X POST \
  http://127.0.0.1:8000/documents/upload \
  -F "file=@document.pdf"
```

---

### Ask a Question

```http
POST /query
```

Example request:

```json
{
  "question": "What is the main topic of the document?"
}
```

Example response:

```json
{
  "answer": "The document mainly discusses...",
  "sources": [
    {
      "document": "document.pdf",
      "page": 2
    }
  ]
}
```

> The exact API routes and response format depend on the implementation.

---

## 🔎 Retrieval Process

The retrieval system searches for document chunks that are semantically similar to the user's question.

For example:

```text
Question:
"What are the benefits of cloud computing?"

              ↓

Embedding Model

              ↓

Vector Search

              ↓

┌────────────────────────────────────┐
│ Chunk 1 - Cloud computing benefits │
│ Chunk 2 - Cloud scalability         │
│ Chunk 3 - Cloud cost reduction     │
└────────────────────────────────────┘

              ↓

Relevant Context

              ↓

LLM

              ↓

Final Answer
```

---

## 📊 RAG Components

| Component | Purpose |
|---|---|
| Document Loader | Reads uploaded documents |
| Text Splitter | Divides documents into smaller chunks |
| Embedding Model | Converts text into vectors |
| Vector Database | Stores and searches embeddings |
| Retriever | Finds relevant document chunks |
| LLM | Generates the final response |
| API | Provides access to the RAG system |

---

## 🧪 Testing

Run the tests using:

```bash
pytest
```

For verbose output:

```bash
pytest -v
```

---

## 🎯 Advantages of RAG

### Reduced Hallucination

The model can use retrieved document information as context instead of relying only on its pretrained knowledge.

### Private Knowledge

Organizations can connect their own documents to the system.

### Up-to-Date Information

New documents can be indexed without retraining the LLM.

### Source-Grounded Answers

Retrieved chunks can be returned along with the generated answer.

### Flexible Knowledge Base

The system can be extended to support multiple document types and knowledge sources.

---

## 🔮 Future Improvements

- [ ] Support PDF, DOCX, TXT and other document formats
- [ ] Add multi-document conversations
- [ ] Add conversation memory
- [ ] Add source citations
- [ ] Add document preview
- [ ] Add authentication
- [ ] Add user-specific document collections
- [ ] Add hybrid search
- [ ] Add reranking
- [ ] Add streaming responses
- [ ] Add chat history
- [ ] Add evaluation metrics for RAG quality
- [ ] Add Docker support
- [ ] Add production monitoring

---

## 📌 Use Cases

This project can be used for:

- 📚 Research document analysis
- 🎓 Educational assistants
- 🏢 Enterprise knowledge bases
- 📄 Document question answering
- ⚖️ Legal document analysis
- 📑 Report analysis
- 🤖 Internal AI assistants
- 🧑‍💻 Developer documentation assistants

---

## 🔒 Security Considerations

- Store API keys in environment variables.
- Never commit `.env` files.
- Validate uploaded files.
- Restrict supported file types.
- Apply file-size limits.
- Authenticate users in production.
- Isolate user-specific documents.
- Avoid exposing sensitive document contents.
- Implement access control for private knowledge bases.

---

## ⚡ Performance Considerations

For larger document collections, performance can be improved through:

- Efficient chunk sizes
- Metadata filtering
- Vector indexes
- Query caching
- Embedding caching
- Retrieval reranking
- Batch document processing
- Asynchronous API operations

---

## 🧩 Example RAG Workflow

```text
                    DOCUMENT
                       │
                       ▼
                Text Extraction
                       │
                       ▼
                  Chunking
                       │
                       ▼
                 Embeddings
                       │
                       ▼
                Vector Store
                       │
                       │
                       │
USER ──► QUESTION ────┘
          │
          ▼
     Similarity Search
          │
          ▼
   Relevant Context
          │
          ▼
         LLM
          │
          ▼
       ANSWER
```

---

## 👨‍💻 Author

**Anshuman Singh**

An AI-focused project demonstrating Retrieval-Augmented Generation, document processing, semantic search, and LLM-powered question answering.

---

## ⭐ Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add new feature"
```

5. Push the branch.

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

## 📄 License

This project is intended for educational and development purposes. Add an appropriate open-source license if you plan to distribute the project publicly.
