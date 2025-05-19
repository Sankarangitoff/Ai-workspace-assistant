import os
import shutil
from app.config import UPLOAD_DIR, FILE_LOADERS, vectorstore
from langchain_community.document_loaders import PyPDFLoader, CSVLoader, TextLoader, UnstructuredWordDocumentLoader, UnstructuredExcelLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from app.config import CHROMA_PATH
from langchain_community.embeddings import HuggingFaceEmbeddings

# Embedding model setup
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_model)

LOADER_MAPPING = {
    "pdf": PyPDFLoader,
    "csv": CSVLoader,
    "txt": TextLoader,
    "docx": UnstructuredWordDocumentLoader,
    "xlsx": UnstructuredExcelLoader
}

def load_and_embed(file_path: str):
    ext = file_path.split(".")[-1].lower()
    loader_class = LOADER_MAPPING.get(ext)
    if not loader_class:
        print(f"Unsupported file type: {ext}")
        return None

    loader = loader_class(file_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    vectorstore.add_documents(chunks)
    return len(chunks)

def get_uploaded_file_path(user_id: str, file_id: str) -> str:
    user_upload_dir = os.path.join(UPLOAD_DIR, user_id)
    if not os.path.exists(user_upload_dir):
        return None
    for fname in os.listdir(user_upload_dir):
        base_name = os.path.splitext(fname)[0]
        if base_name == file_id:
            return os.path.join(user_upload_dir, fname)
    return None 