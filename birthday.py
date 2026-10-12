from datetime import datetime
#Input User birthday date
birth_Day = int(input("Enter your birthday Date between 1 to 31:"))
birth_Month = int(input("Enter your Birthday months between 1 to 12:"))

#curent Date
today = datetime.now()
current_year = today.year

#next birthday
birthDay = datetime(current_year,birth_Month,birth_Day)
if birthDay<today:
    birthDay = datetime(current_year+1, birth_Month, birth_Day)

#days remaining
days_left = (birthDay - today).days
print(f"Your next birthday  is {days_left} days left.")