# 🩺 Medical Research Assistant
[![Hugging Face Space](https://img.shields.io/badge/🤗%20HuggingFace-Live%20Demo-yellow)](https://huggingface.co/spaces/hdtai24/medical-rag-assistant)

A Retrieval-Augmented Generation (RAG) application for querying medical research papers using natural language.

Built with **Streamlit**, **LangChain**, **FAISS**, **Sentence Transformers**, and **Google Gemini**.

---

## 🚀 Features

* 📄 Upload multiple medical research papers (PDF)
* ✂️ Automatic document chunking
* 🔍 Semantic search using FAISS vector database
* 🧠 Context-aware question answering with Gemini
* 📚 Source citation with page references
* ⚡ Fast retrieval using BGE embeddings
* 💬 Chat-style interface
* 🔄 Rebuild knowledge base from uploaded papers

---

## 🏗️ Architecture

```text
PDF Papers
     │
     ▼
PDF Loader
     │
     ▼
Text Chunking
     │
     ▼
BGE Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Retriever
     │
     ▼
Gemini 2.5 Flash
     │
     ▼
Answer + Sources
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### LLM

* Gemini 2.5 Flash

### RAG Framework

* LangChain

### Embedding Model

* BAAI/bge-small-en-v1.5

### Vector Database

* FAISS

### PDF Processing

* PyPDF

---

## 📂 Project Structure

```text
medical-rag-assistant/
│
├── app.py
│
├── backend/
│   ├── build_index.py
│   ├── pdf_loader.py
│   ├── rag_pipeline.py
│   └── vector_store.py
│
├── data/
│   └── *.pdf
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/medical-rag-assistant.git

cd medical-rag-assistant
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

---

## 📚 Build Knowledge Base

Place PDFs inside the `data/` directory.

Run:

```bash
python -m backend.build_index
```

This creates:

```text
faiss_index/
├── index.faiss
└── index.pkl
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 💡 Example Questions

* What is asthma?
* How is wheeze detected?
* What sensors are used for lung sound analysis?
* What machine learning models are proposed?
* What is the implication of the main finding?
* How was the dataset collected?

---

## 📸 Demo

Upload medical papers and ask questions such as:

> What machine learning model achieved the best performance?

The system retrieves relevant passages from the papers and generates an answer grounded in the retrieved evidence.

---

## 🎯 Learning Objectives

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector search with FAISS
* Semantic document retrieval
* LLM integration with Gemini
* Medical document question answering
* End-to-end AI application development

---

## 🌐 Deployment

The application is deployed on Hugging Face Spaces:

https://huggingface.co/spaces/hdtai24/medical-rag-assistant

Users can:
- Upload medical PDFs
- Build a custom knowledge base
- Ask questions using natural language
- Receive evidence-grounded answers with source citations

---

## 👨‍💻 Author

**Tran Huynh Duc Tai**

Graduate Researcher | AI Engineer

Interests:

* Edge AI
* Medical AI
* TinyML
* Deep Learning
* Retrieval-Augmented Generation (RAG)

---

## License

MIT License
