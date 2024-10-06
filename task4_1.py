# функція розраховує кількість днів від сьогоднішньої дати до заданої дати

from datetime import datetime

def get_days_from_today(date_string):
    # формат дати 
    date_format = "%Y-%m-%d"
    # перетворення рядка дати в об'єкт datetime
    input_date = datetime.strptime(date_string, date_format)
    # отримання поточної дати
    today = datetime.today()
    # обчислення різниці між заданою датою і сьогоднішньою датою
    difference = input_date - today
    # повернення кількості днів у вигляді цілого числа  
    return difference.days

# Приклад використання функції
date_input = "2025-06-11"
days = get_days_from_today(date_input)
print (f"Кількість днів від сьогодні до {date_input}: {days}")

