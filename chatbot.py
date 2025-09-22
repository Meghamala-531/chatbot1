# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    # Greeting rules
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! Thanks for asking."

    # About chatbot
    elif "who are you" in user_input or "what are you" in user_input:
        return "I'm a simple rule-based chatbot created in Python."

    # Help rule
    elif "help" in user_input:
        return "Sure! You can ask me about greetings, time, or general questions."

    # Time rule
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    # Goodbye rule
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day 😊"

    # Default response
    else:
        return "I'm not sure I understand. Can you rephrase that?"


# Main program loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break
