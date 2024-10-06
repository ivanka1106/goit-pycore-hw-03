# функція для отримання списку днів народження колег

from datetime import datetime, timedelta

def get_upcoming_birthdays (users):
    today = datetime.today().date() # отримуємо поточну дату
    upcoming_birthdays = [] # список для збереження найближчих днів народження
    
    for user in users:
        # конвертуємо рядок з датою народження у формат  datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # змінюємо рік дати народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)
           
        # якщо день народження припадає на суботу чи неділю, переносимо привітання на понеділок    
        if birthday_this_year.weekday() in (5,6):
            birthday_this_year += timedelta (days=(7-birthday_this_year.weekday()))
         
        # додаємо користувача до списку з датою привітання        
        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": birthday_this_year.strftime("%Y-%m-%d")
            }) 
            
        return upcoming_birthdays
        
# список users
users = [
    {"name": "John Doe", "birthday": "1985.10.07"},
    {"name": "Jane Smith", "birthday": "1990.10.12"},
    {"name": "Nina Black", "birthday": "1991.10.05"}
]
# # Приклад використання функції
        
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

        

        
      