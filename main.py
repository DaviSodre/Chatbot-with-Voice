import openai

openai.api_key = "YOUR API KEY"

nome = "Sofia"

mensagens = [{"role": "system", "content": f"Seu nome é {nome} você é uma inteligencia artificial cômica e sincera, seu criador se chama Davi"},]

def ask_gpt(mensagens, user_input):
    mensagens = mensagens + [{"role": "user", "content": user_input}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=mensagens,
        max_tokens=250,
        temperature=1
    )
    return response['choices'][0]['message']['content']

def main():
    while True:
        user_input = input("Você: ")
        resposta = ask_gpt(mensagens, user_input)
        print(f"{nome}:", resposta)

if __name__ == "__main__":
    main()
