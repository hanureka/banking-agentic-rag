from ingestion.vector_store import load_vector_store

def retrieval_agent(question: str):
    db = load_vector_store()
    docs = db.similarity_search(
        question,
        k=4
    )
    context = "\n".join([
        d.page_content for d in docs
    ])
    return context