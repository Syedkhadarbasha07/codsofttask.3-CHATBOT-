# Rule-Based Chatbot using Python

print("🤖 ChatBot: Hello! I am a rule-based chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    # Greeting
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")

    # Asking name
    elif "your name" in user_input:
        print("Bot: I am a simple rule-based chatbot.")

    # Asking about creator
    elif "who created you" in user_input:
        print("Bot: I was created using Python rules and conditions.")

    # Help
    elif "help" in user_input:
        print("Bot: I can answer simple questions like greetings, time, and basic info.")

    # Time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time is {current_time}")

    # Date
    elif "date" in user_input:
        from datetime import datetime
        today = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {today}")

    # How are you
    elif "how are you" in user_input:
        print("Bot: I'm functioning perfectly! Thanks for asking.")

    # Exit condition
    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day 👋")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand that. Can you try something else?")