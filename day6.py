import os
import random
import datetime
WORDS = ["sova", "sobaka", "papa", "dog", "house", "paper", "sun", "light", "car", "slon"]

def generate_password():
    password = ""
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
    os.path.exists("passwords.txt")
    if os.path.isfile("passwords.txt"):
        with open("passwords.txt", "a") as file:
         for password in passwords:
            file.write(password + "\n")
    else: 
        with open("passwords.txt", "w") as file:
         for password in passwords:
            file.write(password + "\n")

name = input("Введите имя: ")
n = int(input("Сколько паролей сгенерировать? "))

datatime = load_passwords()
print("Загружено паролей: " + str(len(datatime)))

save_passwords([name + " |" +" (" + str(datetime.date.today()) + ") | " + generate_password() for _ in range(n)])
print("Пароли сохранены.")  

for _ in range(n):
    print(generate_password())


