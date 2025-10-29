# Модуль DateTime - работа с датами и временем
# В DateTime входят основные классы Date, Time, DateTime
import datetime # Для today

from  datetime import date,time,datetime # Для today_2
import locale

locale.setlocale(locale.LC_ALL,"")
######## Преобразовать в строку ###########
# strftime(format)

'''
%a: аббревиатура дня недели. Например, Wed - от слова Wednesday (по умолчанию используются английские наименования)

%A: день недели полностью, например, Wednesday

%b: аббревиатура названия месяца. Например, Oct (сокращение от October)

%B: название месяца полностью, например, October

%d: день месяца, дополненный нулем, например, 01

%m: номер месяца, дополненный нулем, например, 05

%y: год в виде 2-х чисел

%Y: год в виде 4-х чисел

%H: час в 24-х часовом формате, например, 13

%I: час в 12-ти часовом формате, например, 01

%M: минута

%S: секунда

%f: микросекунда

%p: указатель AM/PM

%c: дата и время, отформатированные под текущую локаль

%x: дата, отформатированная под текущую локаль

%X: время, форматированное под текущую локаль
'''
date_time_3 = datetime.now()
print(f'Обычный формат даты: {date_time_3}')
a_date_time_3 = date_time_3.strftime('%a')
print(f'аббревиатура дня недели: {a_date_time_3}')
A_date_time_3 = date_time_3.strftime('%A')
print(f'День недели: {A_date_time_3}')
m_date_time_3 = date_time_3.strftime('%B')
print(m_date_time_3)
f_date_time = date_time_3.strftime('%d %B %Y - это день недели %A')
print(f_date_time)
print(type(f_date_time))
date_1 = datetime(2025,12,10, 12,30,55)
print(date_1)
print(date_1.strftime('%d %B %Y'))
print(date_1.year)
print(date_1.month)