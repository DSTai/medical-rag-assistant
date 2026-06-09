from sentence_transformers import CrossEncoder

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)
def rerank(query, docs, top_k=5):

    pairs = [
        (query, doc.page_content)
        for doc in docs
    ]

    scores = reranker.predict(pairs)

    scored_docs = list(zip(docs, scores))

    scored_docs.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return [
        doc
        for doc, score in scored_docs[:top_k]
    ]