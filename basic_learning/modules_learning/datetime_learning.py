from datetime import datetime, date, time, timedelta

today = datetime.today()
now = datetime.now()

print(today)  # 2020-04-05 17:30:29.057350
print(now)  # 2020-04-05 17:30:29.057350
print(now.strftime('%d.%m.%Y - %A'))  # 05.04.2020 - Sunday

print('{0.year}-{0.month}-{0.day}'.format(today))

date_string = '05.04.2020'

date_object = datetime.strptime(date_string, '%d.%m.%Y')

print(date_string, date_object)
print(type(date_string), type(date_object))
