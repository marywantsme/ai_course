import json
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

SYSTEM_PROMPT = """
Ты анализируешь лоты госзакупок на гардеробное обслуживание в Москве.
Получив любую информацию о лоте — сразу анализируй и выдавай результат.
Не задавай уточняющих вопросов. Анализируй то что есть.

Отвечай ТОЛЬКО валидным JSON без markdown, без кавычек, без пояснений:
{"название": "...", "тип_учреждения": "...", "сумма": число, "выгодно": true или false, "риски": ["риск1"], "рекомендация": "..."}
"""

history = []
print("Бизнес-ассистент готов к работе.")
print("Для многострочного ввода — введи текст и нажми Enter дважды.")
print("Напиши 'выход' для завершения.\n")

while True:
    print("\nТы (Enter дважды для отправки):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        if line.lower() == "выход":
            print("До свидания!")
            exit()
        lines.append(line)
    
    user_input = "\n".join(lines)
    
    if not user_input.strip():
        continue
    
    history.append({"role": "user", "content": user_input})
    
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=history
    )
    
    response = message.content[0].text
    clean_response = response.replace("```json", "").replace("```", "").strip()
    history.append({"role": "assistant", "content": response})
    
    try:
        data = json.loads(clean_response)
        print(f"\n{'='*40}")
        print(f"Название: {data['название']}")
        print(f"Тип: {data['тип_учреждения']}")
        print(f"Сумма: {data['сумма']} руб.")
        print(f"Выгодно: {'Да' if data['выгодно'] else 'Нет'}")
        print(f"Риски: {', '.join(data['риски'])}")
        print(f"Рекомендация: {data['рекомендация']}")
        print(f"{'='*40}")
    except json.JSONDecodeError:
        print("Ошибка парсинга:")
        print(clean_response)