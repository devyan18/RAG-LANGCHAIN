from langchain_chroma import Chroma
from src.retriever import chroma_client, INDEX_NAME
from langchain_community.embeddings import OllamaEmbeddings
from src.config import env
from src.chain import chain
from langchain.chains.question_answering import load_qa_chain
from src.llm import llm

# vstore = Chroma(client=chroma_client,
#                 collection_name=INDEX_NAME,
#                 embedding_function=OllamaEmbeddings(
#                 model=env.model,
#             ))


# docs = vstore.similarity_search(question, 5)

# chain = load_qa_chain(llm, chain_type="stuff")

# respuesta = chain.invoke(
#     input=question,
#     context=docs,
# )



# print(respuesta)

def main():
    try:
        if __name__ == "__main__":
            print(env.model)
            print(env.file)

            question = input("Pregunta: ")
            response = chain.invoke(question)
            print(response)
    except KeyboardInterrupt as e:
        print(f"Goodbye! {e}")

main()

# def delete_index():
#     chroma_client.delete_collection(INDEX_NAME)

# delete_index()