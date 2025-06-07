import os
from logger import logger
from config import MODEL_PATH, DATA_PATH
from rag.model import load_llm
from rag.loader import load_documents
from rag.embeddings import build_graph

from agent.reasoning import run_reasoning_loop
from tools import tools

def initialize_rag():
    logger.info("🔄 Initializing RAG...")
    llm = load_llm(MODEL_PATH)
    documents = load_documents(DATA_PATH)
    G, embed_model = build_graph(documents)
    return llm, G, embed_model

if __name__ == "__main__":
    try:
        llm, G, embed_model = initialize_rag()
        logger.info("RAG system initialized successfully")
    except Exception as e:
        logger.error("RAG initialization failed: %s", str(e))
        exit("❌ Error initializing RAG system")

    print("\n🤖 CTF Assistant (CLI mode). Type your question or 'exit' to quit.\n")
    while True:
        user_input = input("❓ Your question: ")
        if user_input.strip().lower() in ("exit", "quit"):
            print("👋 Exiting.")
            break
        try:
            response = run_reasoning_loop(llm=llm, tools=tools, user_question=user_input)
            print("\n💬 Answer:")
            print(response)
            print("-" * 60)
        except Exception as e:
            print(f"❌ Error generating response: {e}")
