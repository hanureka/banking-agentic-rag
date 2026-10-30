# Performs similarity search against ChromaDB
from ingestions.vector_store import load_vector_store


def retrieval_agent(question):

    db = load_vector_store()

    results = db.similarity_search_with_score(
        question,
        k=5
    )

    context = ""

    citations = []

    for doc, score in results:

        context += doc.page_content + "\n\n"

        citations.append(
            {
                "score": round(score, 3),
                "content": doc.page_content[:200]
            }
        )

    return context, citations