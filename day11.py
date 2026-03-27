import requests 
import datetime
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

SYSTEM_PROMPT = """Ты финансовый аналитик. Анализируй курсы валют и давай краткие рекомендации простым языком."""

def get_rates():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    if response.status_code == 200:
        return response.json()
    return None

def convert(amount, data):
    rub = amount * data["rates"]["RUB"]
    eur = amount * data["rates"]["EUR"]
    kzt = amount * data["rates"]["KZT"]
    return rub, eur, kzt

def get_ai_comment(amount, data):
    history = [{
        "role": "user",
        "content": f"Курсы на сегодня: 1 USD = {data['rates']['RUB']} RUB, {data['rates']['EUR']} EUR, {data['rates']['KZT']} KZT. Пользователь конвертирует {amount} USD. Дай краткий комментарий."
    }]
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=history
    )
    return message.content[0].text


data = get_rates()
print(f"Курс на {datetime.date.today()}:")
print(f"1 USD = {data['rates']['RUB']:.2f} RUB")

amount = float(input("\nВведите сумму в USD: "))
rub, eur, kzt = convert(amount, data)

print(f"\n{amount} USD = {rub:.2f} RUB")
print(f"{amount} USD = {eur:.2f} EUR")
print(f"{amount} USD = {kzt:.2f} KZT")

print("\nClaude анализирует...")
comment = get_ai_comment(amount, data)
print(f"\nClaude: {comment}")

