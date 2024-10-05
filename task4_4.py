from datetime import datetime, timedelta

def get_upcoming_birthdays (users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
            
        delta_days = (birthday_this_year - today).days
        if 0<= delta_days <= 7:
            
            if birthday_this_year.weekday() in (5,6):
                birthday_this_year += timedelta (days=(7-birthday_this_year.weekday()))
                
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
        # Використання функції get_upcoming_birthdays
        
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

        

        
      