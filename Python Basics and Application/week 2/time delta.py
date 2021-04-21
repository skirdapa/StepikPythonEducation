import datetime
# Ввод с помощью функции map, которая применяем функцию ко всем списку, в нашем случае лямбду функцию
y, m, d = map(lambda x: int(x), input().split())
delta = datetime.timedelta(int(input()))
my_date = datetime.date(y, m, d)
my_date += delta
print(my_date.strftime("%Y %-m %-d"))
# print(my_date.year, my_date.month, my_date.day) - еще один вариант выводы в формате yyyy m d


