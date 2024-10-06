# функція для нормалізаціі телефонних номерів

import re

def normalize_phone(phone_number):
    
    # видаляємо всі символи, крім цифр і знаку +
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)
    
    # якщо номер починається з '380', додаємо тільки знак '+'
    if cleaned_number.startswith ('380'):
        return '+' + cleaned_number
    
    # якщо номер не містить знаку '+', додаємо міжнародний код '+38'
    elif  not cleaned_number.startswith ('+'):
        return '+38' + cleaned_number
    
    # повераємо очищений номер
    else:
        return cleaned_number

    # Приклад використання функції
    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

   
