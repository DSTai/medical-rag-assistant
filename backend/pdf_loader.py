from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    return docs


def split_docs(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_documents(docs)

    return chunks