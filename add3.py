name = input("Как тебя зовут? ")
print("\nПривет, " + name + "!")

def get_average_mark(marks):
    n = len(marks)
    return sum_marks(marks) / n

def sum_marks(marks):
    total = 0
    for mark in marks:
        total = int(mark) + total
    return total

def get_best_subject(subjects):
    best_mark = 0
    best_subject = ""
    for subject, mark in subjects:
        if int(mark) > best_mark:
            best_mark = int(mark)
            best_subject = subject
    return best_subject, best_mark

def get_worst_subject(subjects):
    worst_mark = 10
    worst_subject = ""
    for subject, mark in subjects:
        if int(mark) < worst_mark:
            worst_mark = int(mark)
            worst_subject = subject
    return worst_subject, worst_mark

n = int(input("\nСколько у тебя предметов? "))
subjects = []

for i in range(n):
    subject = input("Введите название предмета: ")
    marks = input("Введите оценку по этому предмету (1-10): ")
    subjects.append((subject, marks))

print("\nСтудент: " + name + "!")
print("\n-------------- ")
for subject, marks in subjects:
    print(" " + subject + " " + ":" + " " + marks + "")
print(" -------------- ")
all_marks = []
for subject, marks in subjects:
    all_marks.append(marks)
print("\nСредняя оценка: " + str(round(get_average_mark(all_marks), 2)) + "")
print("Лучший предмет: " + get_best_subject(subjects)[0] + " - " + str(get_best_subject(subjects)[1]) + "")
print("Худший предмет: " + get_worst_subject(subjects)[0] + " - " + str(get_worst_subject(subjects)[1]) + "") 