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

def print_contact(contact, number):
     print(format_contact(contact, number))

n = int(input("Сколько контактов? "))
contacts = []

for i in range(n):
    print("\n--- Контакт " + str(i + 1) + " ---")
    person = {}
    person["name"] = input("Введите имя: ")
    person["age"] = input("Введите возраст: ")
    person["city"] = input("Введите город: ")
    person["status"] = get_status(int(person["age"]))
    
    contacts.append(person)

for i in range(len(contacts)):
 print_contact(contacts[i], i + 1)