# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

This guide outlines the steps to set up and run the Physical AI & Humanoid Robotics textbook project, including the Docusaurus frontend and the Python RAG backend.

## Prerequisites

*   **Node.js and npm/yarn**: For Docusaurus frontend development.
*   **Python 3.8+**: For the RAG backend.
*   **Qdrant**: Local or cloud instance for vector storage.
*   **Neon (PostgreSQL)**: Account and connection details for metadata storage.
*   **Google Cloud Account**: For deploying the RAG backend on Cloud Run and using Vertex AI.
*   **GitHub Account**: For hosting frontend on GitHub Pages and backend deployment (optional).

## Setup Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Setup Frontend (Docusaurus)

Navigate to the frontend directory (e.g., `frontend/`) and install dependencies:

```bash
cd frontend/
npm install # or yarn install
```

### 3. Setup Backend (Python RAG)

Navigate to the backend directory (e.g., `backend/`) and set up a virtual environment:

```bash
cd backend/
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

**Environment Variables**: Configure your backend to use your Qdrant, Neon, and Google Cloud credentials. This typically involves setting environment variables (e.g., `QDRANT_URL`, `NEON_DB_URL`, `GCP_PROJECT_ID`, `VERTEX_AI_EMBEDDING_MODEL`, `GEMINI_MODEL_NAME`). A `.env` file is recommended.

### 4. Ingest Textbook Data

Prepare your textbook content (Markdown/MDX files) and place them in the appropriate directory (e.g., `frontend/docs/`). Then, run the data ingestion script to process the content, generate embeddings, and store them in Qdrant and metadata in Neon.

```bash
python ingest_data.py
```

*(Note: `ingest_data.py` script needs to be created as part of implementation.)*

### 5. Run the Development Server

**Frontend**: Start the Docusaurus development server:

```bash
cd frontend/
npm start
```

This will typically run on `http://localhost:3000`.

**Backend**: Start the Python RAG backend API (e.g., using FastAPI): 

```bash
cd backend/
uvicorn main:app --reload
```

This will typically run on `http://localhost:8000`.

## Deployment

### Frontend

Deploy the Docusaurus static site to GitHub Pages. This will involve configuring GitHub Actions to build the site and deploy it to the `gh-pages` branch.

### Backend

Deploy the Python RAG backend to Google Cloud Run. Configure it to use your Qdrant and Neon instances. Ensure CORS is configured correctly to allow requests from your GitHub Pages domain.

## Further Information

Refer to the API documentation (`specs/master/contracts/rag_chatbot_api.yaml`) for details on interacting with the chatbot API.
