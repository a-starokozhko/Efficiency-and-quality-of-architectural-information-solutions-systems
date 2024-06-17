def calculate_score(params):
    # Витягуємо дані зі словника параметрів
    name = params.get('name', '')
    age = params.get('age', 0)
    gender = params.get('gender', '')
    height = params.get('height', 0)
    weight = params.get('weight', 0)
    scores = params.get('scores', [])

    # Бізнес-логіка для розрахунку загального рейтингу
    total_score = sum(scores)

    # Перевірка чи користувач є повнолітнім
    is_adult = age >= 18

    # Виведення результатів
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Height:", height)
    print("Weight:", weight)
    print("Total Score:", total_score)
    print("Adult:", is_adult)

# Приклад виклику функції
params = {
    'name': "John",
    'age': 25,
    'gender': "Male",
    'height': 175,
    'weight': 70,
    'scores': [85, 90, 75, 88, 92]
}

calculate_score(params)
