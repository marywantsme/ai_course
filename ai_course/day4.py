def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(contact["name"] + "," + contact["age"] + "," + contact["city"] + "," + contact["status"] + "\n")

def load_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, age, city, status = line.strip().split(",")
                contact = {"name": name, "age": age, "city": city, "status": status}
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
    result = result + "Возраст: " + contact["age"] + "\n"
    result = result + "Город: " + contact["city"] + "\n"
    result = result + "Статус: " + contact["status"] + "\n"
    return result

contacts = load_contacts()
print("Загружено контактов: " + str(len(contacts)))
loaded_count = len(contacts)

n = int(input("Сколько новых контактов добавить? "))

for i in range(n):
    print("\n--- Новый контакт " + str(loaded_count + i + 1) + " ---")
    person = {}
    person["name"] = input("Введите имя: ")
    person["age"] = input("Введите возраст: ")
    person["city"] = input("Введите город: ")
    person["status"] = get_status(int(person["age"]))
    contacts.append(person)

loaded_count = len(contacts)
    
    
for i in range(len(contacts)):
    print(format_contact(contacts[i], i + 1))

save_contacts(contacts)
print("Контакты сохранены.")
