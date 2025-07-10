import openai

# Set up OpenAI API key
openai.api_key = "your-api-key-here"

def chat_with_ai(user_input):
    """Generate AI response using OpenAI's GPT model."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

print("Welcome to the Educational Chatbot! Ask me anything.")
while True:
    query = input("You: ")
    if query.lower() == "exit":
        print("krisk")
        break
    answer = chat_with_ai(query)
    print("AI:", answer)