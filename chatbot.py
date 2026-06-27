print("=" * 50)
print("🤖 WELCOME TO ALPHABOT")
print("=" * 50)
print("Type 'bye' anytime to exit.\n")

while True:

    user = input("😊 You: ").lower()

    if user == "hello":
        print("🤖 AlphaBot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("🤖 AlphaBot: I'm doing great. Thanks for asking!")

    elif user == "what is your name":
        print("🤖 AlphaBot: My name is AlphaBot.")

    elif user == "who created you":
        print("🤖 AlphaBot: I was created using Python.")

    elif user == "what can you do":
        print("🤖 AlphaBot: I can answer simple questions and chat with you.")

    elif user == "thank you":
        print("🤖 AlphaBot: You're welcome!")

    elif user == "bye":
        print("🤖 AlphaBot: Goodbye! Have a great day.")
        break

    else:
        print("🤖 AlphaBot: Sorry, I don't understand that.")