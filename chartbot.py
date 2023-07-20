# Rule-based chatbot
def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define rules and corresponding responses
    if user_input in ['hello', 'hi', 'hey', 'hola']:
        return "Hello there! How can I assist you today?"

    elif 'your name' in user_input:
        return "I am a simple chatbot. You can call me ChatGPT."

    else:
        return "I'm sorry, I don't understand that. Can you please rephrase or ask something else?"

# Main function to run the chatbot
def main():
    print("Chatbot: Hi, I'm ChatGPT. Feel free to ask me anything!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day.")
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

