from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings


EMBED_MODEL = "BAAI/bge-small-en-v1.5"
INDEX_PATH = "faiss_index"

def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name=EMBED_MODEL
    )


def create_vector_db(chunks):

    embeddings = get_embeddings()

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_db


def save_vector_db(vector_db):

    vector_db.save_local(INDEX_PATH)


def load_vector_db():

    embeddings = get_embeddings()

    db = FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db