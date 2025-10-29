# Строку в DateTime

from datetime import datetime

str = '25/01/09'
print(str)
#######
date = datetime.strptime(str,'%y/%d/%m')
print(date)
str_2 = '29.10.2025'
date_1 = datetime.strptime(str_2,'%d.%m.%Y')
print(date_1)
str_3 = '31-12-2025 23. 30. 00'
date_2 = datetime.strptime(str_3, '%d-%m-%Y %H. %M. %S')
print(date_2)
print(type(date_2))