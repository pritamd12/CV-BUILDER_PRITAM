import ollama

print("=" * 50)
print("      OFFLINE AI CHATBOT")
print("      Powered by Ollama + Llama 3.2")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        print("\nAI : Goodbye!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("\nAI :")
    print(response["message"]["content"])