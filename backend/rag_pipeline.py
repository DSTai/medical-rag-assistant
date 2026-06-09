import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from backend.vector_store import load_vector_db
from backend.reranker import rerank

load_dotenv()


class MedicalRAG:

    def __init__(self):

        self.db = load_vector_db()

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0
        )

    def ask(self, query):

        docs = self.db.similarity_search(
            query,
            k=10
        )

        docs = rerank(
            query,
            docs,
            top_k=3
        )

        sources = []

        for doc in docs:

            page = doc.metadata.get("page", "unknown")

            sources.append(
                f"Page {page + 1}"
            )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
            Answer ONLY using the context.

            Context:
            {context}

            Question:
            {query}

            Provide a concise answer.
            """

        response = self.llm.invoke(prompt)

        answer = response.content

        return answer, docs
    
    def ask_with_contexts(self, query):
        docs = self.db.similarity_search(query, k=20)

        docs = rerank(query, docs, top_k=5)

        context_texts = [doc.page_content for doc in docs]

        context = "\n\n".join(context_texts)

        prompt = f"""
        Answer ONLY using the context.

        Context:
        {context}

        Question:
        {query}

        Provide a concise answer.
        """

        response = self.llm.invoke(prompt)

        return {
            "answer": response.content,
            "contexts": context_texts,   
            "docs": docs
        }