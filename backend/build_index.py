import os

from backend.pdf_loader import load_pdf
from backend.pdf_loader import split_docs

from backend.vector_store import (
    create_vector_db,
    save_vector_db
)


def build_index():

    all_docs = []

    print("Loading PDFs...")

    for file in os.listdir("./data"):

        if file.endswith(".pdf"):

            path = os.path.join(
                "./data",
                file
            )

            print(f"Loading {file}")

            docs = load_pdf(path)

            for doc in docs:
                doc.metadata["source"] = file

            all_docs.extend(docs)

    print(f"Total pages: {len(all_docs)}")

    print("Chunking...")

    chunks = split_docs(all_docs)

    print(f"Total chunks: {len(chunks)}")

    print("Building FAISS...")

    vector_db = create_vector_db(chunks)

    print("Saving index...")

    save_vector_db(vector_db)

    print("DONE")


if __name__ == "__main__":
    build_index()