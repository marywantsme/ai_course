name = input("Как тебя зовут? ")
age = input("Сколько тебе лет? ")
year = input("Какой сейчас год? ")

print("Привет, " + name + "!")
print("Твой возраст: " + age)
year_2030 = (2030 - int(year)) + int(age)
print("В 2030 году тебе будет: " + str(year_2030))
if int(age) % 2 == 0:
    print("Твой возраст (" + age + ") - четный.") 
else:
    print("Твой возраст (" + age + ") - нечетный.") 
if int(age) < 18:
    print("Ты несовершеннолетний.")
elif int(age) <= 65:
    print("Ты в рабочем возрасте.")
else:
    print("Ты на пенсии.")                                      