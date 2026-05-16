# retriever.py
import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# ── Config ────────────────────────────────────────────
CHROMA_PATH = "./chroma_db"
COLLECTION  = "my_knowledge_base"

# ── Models ────────────────────────────────────────────
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    encode_kwargs={"normalize_embeddings": True}
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0
)

# ── Vector store ──────────────────────────────────────
def load_vector_store():
    if not os.path.exists(CHROMA_PATH):
        raise FileNotFoundError(
            "Vector store not found. Run indexer.py first."
        )
    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_model,
        collection_name=COLLECTION
    )

# ── Format retrieved docs ─────────────────────────────
def format_docs(docs):
    if not docs:
        return "No relevant documents found."
    parts = []
    for i, doc in enumerate(docs):
        source = doc.metadata.get("source", "unknown")
        page   = doc.metadata.get("page", "?")
        parts.append(
            f"[Document {i+1} | Source: {os.path.basename(source)} | Page: {page}]\n"
            f"{doc.page_content}"
        )
    return "\n\n---\n\n".join(parts)

# ── Prompt template ───────────────────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful and accurate assistant.
Your job is to answer questions based STRICTLY on the provided context documents.

Rules:
1. Answer ONLY from the context — never use outside knowledge
2. Always cite which document your answer comes from
3. If the answer is not in the context, say exactly:
   "I don't have information about this in the provided documents."
4. Be concise and direct
5. If context is partially helpful, share what you found and note it may be incomplete"""),

    ("human", """Context Documents:
{context}

Question: {question}

Answer:""")
])

# ── Build RAG chain ───────────────────────────────────
def build_rag_chain(vector_store):
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 3,
            "fetch_k": 10,
            "lambda_mult": 0.7
        }
    )

    chain = (
        {
            "context":  retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

# ── Single question answer ────────────────────────────
def ask(chain, question):
    print(f"\n🙋 Question: {question}")
    print("🤖 Answer:", end=" ")
    response = chain.invoke(question)
    print(response)
    return response
