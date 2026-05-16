# indexer.py
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# ── Config ────────────────────────────────────────────
DOCS_PATH      = "./documents"
CHROMA_PATH    = "./chroma_db"
COLLECTION     = "my_knowledge_base"
CHUNK_SIZE     = 500
CHUNK_OVERLAP  = 50

# ── Embedding model ───────────────────────────────────
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    encode_kwargs={"normalize_embeddings": True}
)

def load_documents():
    """Load all PDFs from documents folder"""
    print("📂 Loading documents...")
    loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    print(f"   Loaded {len(documents)} pages from {DOCS_PATH}")
    return documents

def chunk_documents(documents):
    """Split documents into chunks"""
    print("✂️  Chunking documents...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks = splitter.split_documents(documents)
    print(f"   Created {len(chunks)} chunks")
    return chunks

def build_vector_store(chunks):
    """Embed chunks and store in Chroma"""
    print("🗄️  Building vector store...")
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION,
        collection_metadata={"hnsw:space": "cosine"}
    )
    count = vector_store._collection.count()
    print(f"   Stored {count} chunks in Chroma at {CHROMA_PATH}")
    return vector_store

def index():
    """Run full indexing pipeline"""
    if os.path.exists(CHROMA_PATH):
        print("✅ Vector store already exists. Delete ./chroma_db to re-index.")
        return

    documents  = load_documents()
    chunks     = chunk_documents(documents)
    vector_store = build_vector_store(chunks)
    print("\n✅ Indexing complete!")
    return vector_store

if __name__ == "__main__":
    index()
