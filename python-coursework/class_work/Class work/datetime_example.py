from datetime import date,time,datetime,timedelta

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

print(date(2001,2,3))
print(time(12,30,45))

now = datetime.now()
print(now)
print(now.year)
print(now.day)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)

print(now.strftime('%y-%m-%d'))
print(now.strftime('%d/%m/%y'))
print(now.strftime('%d/%m/%y %H: %M %S'))
print(now.strftime('%B %d %Y %H: %M %S'))
print(now.strftime('%B %d %Y %H: %M %S %p'))
print(now.strftime('%a %B %d %Y %H: %M %S %p'))
print(now.strftime('%A %B %d %Y %H: %M %S %p'))
print(now.strftime('%A %B %d %Y %I: %M %S %p'))



# 0-mon,1-tues,2-wed..7
'''
2025-08-13
2025
8
13
2
3
2001-02-03
12:30:45
2025-08-13 09:12:27.084543
2025
13
8
9
12
27
25-08-13
13/08/25
13/08/25 09: 12 27
August 13 2025 09: 12 27
August 13 2025 09: 12 27 AM
Wed August 13 2025 09: 12 27 AM
Wednesday August 13 2025 09: 12 27 AM
Wednesday August 13 2025 09: 12 27 AM

=== Code Execution Successful ===
'''
from datetime import date,time,datetime,timedelta
today = date.today()
print(today)

now = datetime.now()
print(now)
future = today + timedelta(days = 10) # Front days
print(future)

future = today - timedelta(days = 10) # Back days
print(future)

future = today - timedelta(weeks = 10) # Back days
print(future)

futuretime = now + timedelta(minutes = 30)
futurehour = now + timedelta(hours = 3)

print(futuretime,futurehour)

'''
2025-08-13
2025-08-13 09:18:20.675334
2025-08-23
2025-08-03
2025-06-04
2025-08-13 09:48:20.675334 2025-08-13 12:18:20.675334
'''
