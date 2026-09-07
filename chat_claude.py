from anthropic import Anthropic

# Initialize the client and model
client = Anthropic()
model = "claude-sonnet-4-6"

# Helper functions
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

# Main usage
if __name__ == "__main__":
    messages = []
    
    add_user_message(messages, "Define quantum computing in one sentence")
    answer = chat(messages)
    add_assistant_message(messages, answer)
    print("User: Define quantum computing in one sentence")
    print("Claude:", answer)
    
    add_user_message(messages, "Write another sentence")
    final_answer = chat(messages)
    print("\nUser: Write another sentence")
    print("Claude:", final_answer)
