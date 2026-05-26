def greet():
    return "Hello! Haider 👋 How can I help you today?"

def ask_name():
    return "I am a simple chatbot created for internship tasks 🤖"

def how_are_you():
    return "I'm doing great! Thanks for asking 😊"

def goodbye():
    return "Goodbye! Have a nice day! 👋"

def my_name():
    return "your name is Haider Ali Shah"

def unknown():
    return "Sorry, I didn't understand that. Can you try something else?"

def chatbot():
    print("🤖 Chatbot is running... (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ").lower()

        # Greeting
        if user_input in ["hello", "hi", "hey"]:
            print("Bot:", greet())

        # Asking name
        elif "your name" in user_input:
            print("Bot:", ask_name())

        # How are you
        elif "how are you" in user_input:
            print("Bot:", how_are_you())

        # Help
        elif "help" in user_input:
            print("Bot: Sorry i can't help you! i created jsut  for simple internship task.")
            
        elif "what is my name" in user_input:
            print("Bot:", my_name())

        # Exit
        elif user_input in ["bye", "exit", "quit"]:
            print("Bot:", goodbye())
            break

        # Default
        else:
            print("Bot:", unknown())


# Run chatbot
chatbot()