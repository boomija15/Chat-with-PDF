# Chat-with-PDF
Chat with PDF is a simple LLM based pdf chatbot where users can upload their pdfs and ask questions about it. It used LangChain. FAISS and HiggingFace Embeddings to build a Retrieval Augmented Generation(RAG) pipeline. It also provides a user-friendly interface using Streamlit. 


Key Features:

1. Upload a PDF file through the web interface

2. Automatically processes the document and splits it into semantic chunks

3. Uses sentence-transformers (MiniLM) for embedding the text

4. Stores and retrieves relevant chunks using FAISS vector database

5.  Enables conversation using ChatOllama (Mistral model)

Tech Stack: 
1. Frontend: Streamlit
2. Backend / LLM: LangChain, ChatOllama (Mistral)
3. Embeddings: HuggingFace (MiniLM)
4. Vector Store: FAISS
5. PDF Parsing: LangChain’s PyPDFLoader
