n = int(input("Сколько человек будет в списке? "))
names = []
for i in range(n):
    names.append(input("Введите имя: "))
for i in range(len(names)):
    print(str(i + 1) + ". " + names[i])
if  n % 100 in [11, 12, 13, 14]:
    print("Всего в группе: " + str(n) + " - человек.")  
elif n % 10 in [2, 3, 4]:
    print("Всего в группе: " + str(n) + " - человека.")
else:    print("Всего в группе: " + str(n) + " - человек.")
