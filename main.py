from src.config import env
from src.chain import chain

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