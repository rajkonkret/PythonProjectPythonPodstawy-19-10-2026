from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2026-10-21

time = datetime.now()
print(time)  # 2026-10-21 12:47:39.568523

print(type(today))  # <class 'datetime.date'>
print(type(time))  # <class 'datetime.datetime'>

print(today.day)  # 21
"Return day of the week, where Monday == 0 ... Sunday == 6."
print(today.weekday())  # 2 - środa
"Return day of the week, where Monday == 1 ... Sunday == 7."
print(today.isoweekday())  # 3 - środa
print(today.year)  # 2026

# formatowanie dat
print(today.strftime("%A"))  # Wednesday

formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 21/10/2026
print(type(formated_date))  # <class 'str'>

# 12:57
# 12:57:34
# 12:57 pm
