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

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 13:00
print(type(formated_time))  # <class 'str'>

formated_time_usa = datetime.now().strftime("%I:%M %p")
print(formated_time_usa)  # 01:01 PM
print(formated_time_usa.removeprefix("0"))  # 1:02 PM
print(type(formated_time_usa))  # <class 'str'>

object_data = datetime.now().strptime("21/10/2026", "%d/%m/%Y")
print(object_data)  # 2026-10-21 00:00:00
print(type(object_data))  # <class 'datetime.datetime'>

# tomorrow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2026-10-22

products = [
    {"sku": 1, 'exp_date': today, "price": 200},
    {"sku": 2, 'exp_date': today, "price": 300},
    {"sku": 3, 'exp_date': tomorrow, "price": 400},
    {"sku": 4, 'exp_date': today, "price": 1200},
    {"sku": 5, 'exp_date': today, "price": 900},
    {"sku": 6, 'exp_date': tomorrow, "price": 200.99},
    {"sku": 7, 'exp_date': today, "price": 100},
]
