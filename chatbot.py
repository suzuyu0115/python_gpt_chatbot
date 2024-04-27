import openai

openai.api_key = 'your-api-key'

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "こちらにGPTの役割を記載"}, {"role": "user", "content": prompt}]
    )

    for message in response['choices'][0]['message']['content']:
        if message['role'] == 'assistant':
            print(f"ChatGPT: {message['content']}")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting chat...")
        break
    chat_with_gpt(user_input)
    print("\nNew Chat")
