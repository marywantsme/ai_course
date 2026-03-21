import os
import datetime 

QUESTIONS = [
    {"question": "Столица Франции?", "answer": "париж"},
    {"question": "Сколько дней в неделе?", "answer": "7"},
    {"question": "2 + 2 * 2 = ?", "answer": "6"},
    {"question": "Какой модуль Python генерирует случайные числа?", "answer": "random"},
    {"question": "Что делает len()?", "answer": "длину"},
]
input("Нажмите Enter, чтобы начать викторину...")
score = 0

def run_quiz():
    score = 0
    for q in QUESTIONS:
        answer = input(q["question"] + " ")
        if answer.lower() == q["answer"]:
            print("Правильно!")
            score += 1
        else:
         print("Неправильно. Правильный ответ: " + q["answer"])
    print("Ваша итоговая оценка: " + str(score) + "/" + str(len(QUESTIONS)))      
    return score

def load_results():
    results = []
    try:
        with open("quiz_results.txt", "r") as file:
            for line in file:
                results.append(line.strip())
    except FileNotFoundError:
        pass
    return results

namestr = input("Введите имя: ")     

score = run_quiz()  

with open("quiz_results.txt", "a") as file:
    file.write(namestr + " | " + str(datetime.date.today()) + " | " + str(score) + "/" + str(len(QUESTIONS)) + "\n")
print("Результаты сохранены в quiz_results.txt")    

