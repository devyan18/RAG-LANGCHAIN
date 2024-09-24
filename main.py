from src.chain import chain

question = "¿De qué cripto sistemas habla el documento?"

def main():
    try:
        if __name__ == "__main__":
            response = chain.invoke(question)
            print(response)
    except KeyboardInterrupt as e:
        print(f"Goodbye! {e}")

main()