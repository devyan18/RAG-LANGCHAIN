from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from src.helpers import TextActions
from src.config import env

class VectorDB:
    def __init__(self, chucks):
        self._vector_store = Chroma.from_texts(
            texts=chucks,
            embedding=OllamaEmbeddings(
                model=env.model
            ),
        )

    @property
    def retriever(self):
        return self._vector_store.as_retriever()

pdf_file = env.file
pdf_text = TextActions.extract_text_from_pdf(pdf_file)

chucks = TextActions.split_chucks(pdf_text)

db = VectorDB(chucks=chucks)

retriever = db.retriever