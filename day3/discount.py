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

for p in products:
    # print(p) # {'sku': 7, 'exp_date': datetime.date(2026, 10, 21), 'price': 100}
    print(p['exp_date'])

    if p['exp_date'] == today:
        pass

    if p['exp_date'] != today:
        continue  # konzy bieżące wykonanie pętli, pobiera kolejny element

    print(p['price'])

    p['price'] *= 0.8  # price = price * 0.8
    print(f"""
Price for sku: {p['sku']}
is now: {p['price']:.2f}
""")

    # 2026-10-22
    # 2026-10-21
    # 200
    #
    # Price for sku: 1
    # is now: 160.00
    #
    # 2026-10-21
    # 300
    #
    # Price for sku: 2
    # is now: 240.00
    #
    # 2026-10-22
    # 2026-10-21
    # 1200
    #
    # Price for sku: 4
    # is now: 960.00
    #
    # 2026-10-21
    # 900
    #
    # Price for sku: 5
    # is now: 720.00
    #
    # 2026-10-22
    # 2026-10-21
    # 100
    #
    # Price for sku: 7
    # is now: 80.00
