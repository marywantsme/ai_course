def count_characters(text):
    return len(text)

def count_words(text):
    return len(text.split())

def count_unique_words(text):   
    return len(set(text.split()))   

def most_frequent_word(text):   
    return max(set(text.split()), key=text.split().count)

def to_uppercase(text):
    return text.upper() 

def reverse_text(text):  
    return text[::-1]   

text = input("Введите текст: ")

print(f"Текст: {text}")
print(f"{'-' * 33}")

print(f"Символов: {count_characters(text)}")
print(f"Слов: {count_words(text)}") 
print(f"Уникальных слов: {count_unique_words(text)}")
print(f"Самое частое слово: {most_frequent_word(text)}")
print(f"Текст в верхнем регистре: {to_uppercase(text)}")
print(f"Перевернутый текст: {reverse_text(text)}")