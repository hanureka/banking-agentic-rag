from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config.settings import CHROMA_PATH

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

def create_vector_store(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)
    db = Chroma.from_texts(
        texts=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )
    db.persist()
    return db

def load_vector_store():
    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_model
    )