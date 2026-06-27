# Simple Rule-Based Chatbot

print("🤖 Chatbot: Hi! I'm your chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("🤖 Chatbot: Hello! How can I help you?")

    elif user == "how are you":
        print("🤖 Chatbot: I'm fine! What about you?")

    elif user == "your name":
        print("🤖 Chatbot: I am a simple CLI chatbot.")

    elif user == "what can you do":
        print("🤖 Chatbot: I can answer basic questions!")

    elif user == "help":
        print("🤖 Chatbot: Try asking greetings or simple questions.")

    elif user == "bye":
        print("🤖 Chatbot: Goodbye! 👋")
        break

    else:
        print("🤖 Chatbot: Sorry, I don't understand.")