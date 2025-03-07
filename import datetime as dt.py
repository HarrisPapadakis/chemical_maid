 import datetime as dt
 now = dt.datetime.now()
 birthdatetime = dt.datetime(1995, 3, 31, 8, 26)
 age = now - birthdatetime
 print(age)
 print(type(age))
 8634 days, 7:55:07.739804
 <class 'datetime.timedelta'