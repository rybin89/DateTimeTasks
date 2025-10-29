# Действия над datetime

from datetime import datetime,timedelta

# метод timedelta([days],[seconds] ...) промежутки

three_hours = timedelta(hours=3)
print(three_hours)
now = datetime.now()
print(now)
print(now + three_hours)
new_year = datetime(2026,1,1,0,0,0)
print(new_year - now)