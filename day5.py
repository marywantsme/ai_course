def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(contact["name"] + "," + contact["phone"] + "," + contact["age"] + "," + contact["city"] + "," + contact["status"] + "\n")

def load_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, age, city, status = line.strip().split(",")
                contact = {"name": name, "phone": phone, "age": age, "city": city, "status": status}
                contacts.append(contact)
    except FileNotFoundError:
        pass
    return contacts
    
def get_status(age):
    if age < 18:
        return "Несовершеннолетний"
    elif age <= 65:
        return "Рабочий возраст"
    else:
        return "Пенсия"
    
def format_contact(contact, number):
    result = "\n--- Контакт " + str(number) + " ---\n"
    result = result + "Имя: " + contact["name"] + "\n"
    result = result + "Телефон: " + contact["phone"] + "\n"
    result = result + "Возраст: " + contact["age"] + "\n"
    result = result + "Город: " + contact["city"] + "\n"
    result = result + "Статус: " + contact["status"] + "\n"
    return result

def popcontact(contacts):
    n = int(input("Какой контакт удалить? (введите номер) "))
    if n < 1 or n > len(contacts):
        print("Некорректный номер контакта.")
        return
    name = contacts[n - 1]["name"]
    contacts.pop(n - 1)
    print("Контакт (" + name + ") удален.")

contacts = load_contacts()
print("Загружено контактов: " + str(len(contacts)))
loaded_count = len(contacts)

print("Хотите удалить контакт? (да/нет)")
answer = input().lower()
if answer == "да":
    popcontact(contacts)

n = int(input("Сколько новых контактов добавить? "))

for i in range(n):
    print("\n--- Новый контакт " + str(loaded_count + i + 1) + " ---")
    person = {}
    person["name"] = input("Введите имя: ")
    person["phone"] = input("Введите телефон: ")
    person["age"] = input("Введите возраст: ")
    person["city"] = input("Введите город: ")
    person["status"] = get_status(int(person["age"]))
    contacts.append(person)

loaded_count = len(contacts)
    
    
for i in range(len(contacts)):
    print(format_contact(contacts[i], i + 1))

save_contacts(contacts)
print("Контакты сохранены.")
print("Всего контактов: " + str(len(contacts)))