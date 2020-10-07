import datetime

"""
Python Date
x = datetime.datetime.now()
print(x)
"""

"""
Date Output
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

"""

"""
Creating Date Object
x = datetime.datetime(2020, 5, 17)

print(x)

"""

"""
Display the name of the month
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
"""

x = datetime.datetime.now()

print(x.strftime("%a"))

print(x.strftime("%A"))

print(x.strftime("%w"))

print(x.strftime("%d"))

print(x.strftime("%b"))

print(x.strftime("%B"))

print(x.strftime("%m"))

print(x.strftime("%y"))

print(x.strftime("%Y"))

print(x.strftime("%H"))

print(x.strftime("%I"))

print(x.strftime("%p"))

print(x.strftime("%M"))

print(x.strftime("%S"))

print(x.strftime("%f"))

print(x.strftime("%z"))

print(x.strftime("%Z"))

print(x.strftime("%j"))

print(x.strftime("%U"))

print(x.strftime("%W"))

print(x.strftime("%c"))

print(x.strftime("%x"))

print(x.strftime("%X"))

print(x.strftime("%%"))

"""

from datetimerange import DateTimeRange
time_range = DateTimeRange("2015-03-22T10:00:00+0900", "2020-03-22T10:10:00+0900")
str(time_range)

"""
