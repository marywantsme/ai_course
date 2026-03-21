contacts = [
    {"name": "Алекс", "age": 25},
    {"name": "Аня", "age": 15},
    {"name": "Иван", "age": 30},
    {"name": "Катя", "age": 12},
]

def get_adults (contacts):
    adults = []
    for c in contacts:
        if c["age"] > 18:
            adults.append(c)
    return adults

print("Взрослые: " + ", ".join(str(a["name"]) for a in get_adults(contacts))) 