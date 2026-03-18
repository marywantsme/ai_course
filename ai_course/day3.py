def print_contact(contact, number):

    print("\n---Контакт " + str(number) + " ---")
    print("Имя: " + contact["name"])
    print("Возраст: " + contact["age"])
    print("Город: " + contact["city"])

n = int(input("Сколько контактов? "))
contacts = []

 
for i in range(n):
    print("\n--- Контакт " + str(i + 1) + " ---")
    person = {}
    person["name"] = input("Введите имя: ")
    person["age"] = input("Введите возраст: ")
    person["city"] = input("Введите город: ")
    contacts.append(person)


for i in range(len(contacts)):
    print_contact(contacts[i], i + 1)


