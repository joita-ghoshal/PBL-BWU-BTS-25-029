#chatbot

print("FAQ Chatbot")
print("Type 'bye' to exit")

while True:
    question = input("You: ").lower()

    if question == "hello" or question == "hi":
        print("Bot: Hello! How can I help you?")

    elif "name" in question:
        print("Bot: My name is FAQ Chatbot.")

    elif "college" in question:
        print("Bot: Our college provides quality education.")

    elif "course" in question:
        print("Bot: We offer different courses for students.")

    elif "time" in question:
        print("Bot: College timing is 9 AM to 4 PM.")

    elif question == "bye":
        print("Bot: Goodbye!")

    else:
        print("Bot: Sorry, I don't understand that question.")