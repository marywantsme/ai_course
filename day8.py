import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

history = []

while True:
    user_input = input("\nТы: ")
    
    if user_input.lower() == "выход":
        print("До свидания!")
        break
    
    history.append({"role": "user", "content": user_input})
    
    message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system="Ты helpful ассистент. Всегда отвечай только на русском языке. Будь краток и по делу.",
    messages=history
)
    response = message.content[0].text

    history.append({"role": "assistant", "content": response})
    
    print(f"\nClaude: {response}")