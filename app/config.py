import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()

# API Keys and Config
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Directory paths
UPLOAD_DIR = "data/uploaded_docs"
MEMORY_PATH = "data/memory"
FEEDBACK_PATH = "data/feedback"
USERS_PATH = "data/users"
CHROMA_PATH = "db/chroma"

# Create directories
for path in [UPLOAD_DIR, MEMORY_PATH, FEEDBACK_PATH, USERS_PATH, CHROMA_PATH]:
    os.makedirs(path, exist_ok=True)

# File paths
USER_FILE = os.path.join(USERS_PATH, "users.json")

# Embedding setup
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_model)

# File loaders mapping
FILE_LOADERS = {
    "pdf": "PyPDFLoader",
    "csv": "CSVLoader",
    "txt": "TextLoader",
    "docx": "UnstructuredWordDocumentLoader",
    "xlsx": "UnstructuredExcelLoader"
} 