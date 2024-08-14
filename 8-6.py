from datetime import date
day_now = date.today()
print(day_now)

xday = date(1980, 1, 1)
td = day_now - xday
print(td)

from datetime import datetime
now = datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

dum_day = datetime(2019, 5, 1, hour=15,minute=15, second=15, microsecond=0)
print(dum_day)

dt = datetime.strptime("21/11/2006 16:30", "%d/%m/%Y %H:%M")
print(dt)

dt2 = dt.strftime("%Y年%m月%d日 %H時%M分")
print(dt2)

import datetime
t_delta = detetime.timedelta(days=1)
dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt + t_delta)
