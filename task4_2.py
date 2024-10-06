# функція генерує лотерейний квиток з випадковими числами

import random

def get_numbers_ticket(min_num, max_num, quantity):
    
    # перевірка на правильність ведених параметрів
    if not (1 <= min_num <= max_num <= 1000):
        return []
    
    if not (min_num <= quantity <= max_num):
        return []
    # генеруємо випадкові числа з вказаного діапазону
    random_numbers = random.sample(range(min_num, max_num + 1), quantity)
    # повертаємо відсотртований список
    return sorted (random_numbers)


# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

    


