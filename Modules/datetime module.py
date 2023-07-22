import datetime
mytime = datetime.time(2,30)           #hour, min, sec, microsecond, timezone info
print(mytime.hour)
print(mytime.microsecond)              #it will automatically fill in microseconds
print('\n')

mytimes = datetime.time(13,20,1,20)
print(mytimes.minute)
print(mytimes.microsecond)
print(mytimes)
print('\n')

today = datetime.date.today()
print(today)
print('\n')

print(today.ctime())
print('\n')

mydatetime = datetime.datetime(2021,7,23,14,32,21)
print(mydatetime)
print('\n')


date1 = datetime.date(2001,5,21)
date2 = datetime.date(2001,1,6)
result= date1 - date2
print(result)
print(type(result))
print('\n')


from datetime import datetime               #for showing date and time both
mydatetime = datetime(2021,7,23,14,32,21)
print(mydatetime)
print('\n')

mydatetime= mydatetime.replace(year=2022)
print(mydatetime)
print('\n')


