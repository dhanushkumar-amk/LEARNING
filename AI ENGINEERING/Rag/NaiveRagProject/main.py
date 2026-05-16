# main.py
from indexer import index
from retriever import load_vector_store, build_rag_chain, ask

def main():
    print("=" * 50)
    print("         NAIVE RAG SYSTEM")
    print("=" * 50)

    # Phase A: Index (skips if already done)
    index()

    # Phase B: Load and query
    print("\n📦 Loading vector store...")
    vector_store = load_vector_store()

    print("⛓️  Building RAG chain...")
    chain = build_rag_chain(vector_store)

    print("\n✅ RAG system ready!")
    print("Type 'quit' to exit\n")
    print("-" * 50)

    # ── Conversation loop ─────────────────────────────
    while True:
        question = input("\n🙋 Your question: ").strip()

        if question.lower() in ["quit", "exit", "q"]:
            print("👋 Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        ask(chain, question)

if __name__ == "__main__":
    main()
