# Завдання 1

from datetime import datetime

def get_days_from_today(date_string):

    date_format = "%Y-%m-%d"
    input_date = datetime.strptime(date_string, date_format)
    
    today = datetime.today()
    
    difference = input_date - today
    return difference.days

date_input = "2025-06-11"
days = get_days_from_today(date_input)
print (f"Кількість днів від сьогодні до {date_input}: {days}")

