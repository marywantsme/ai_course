import random
import datetime
WORDS = ["sova", "sobaka", "papa", "dog", "house", "paper", "sun", "light", "car", "slon"]

def generate_password():
    word = random.choice(WORDS)
    symbol = random.choice(("!", "@", "#", "$", "%"))
    number = random.randint(10, 99)
    anotherword = random.choice(WORDS)
    password = word + "_" + anotherword + str(number) + symbol
    return password

def load_passwords():
    passwords = []
    try:
        with open("passwords.txt", "r") as file:
         for line in file:
          passwords.append(line.strip())
    except FileNotFoundError:
        pass
    return passwords

def save_passwords(passwords):
    with open("passwords.txt", "a") as file:
        for password in passwords:
            file.write(password + "\n")

name = input("Введите имя: ")
n = int(input("Сколько паролей сгенерировать? "))

existing_passwords = load_passwords()
print("Загружено паролей: " + str(len(existing_passwords)))

new_passwords = [generate_password() for _ in range(n)]

save_passwords([name + " | " + str(datetime.date.today()) + " | " + p for p in new_passwords])
for p in new_passwords:
    print(p)


