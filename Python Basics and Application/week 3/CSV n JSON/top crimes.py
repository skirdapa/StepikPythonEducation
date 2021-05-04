"""
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""
import csv
import datetime

# type_crime_counter = {}
# with open("Crimes.csv", "r") as crimes:  # Открываем наш файл для чтения:
#     reader = csv.DictReader(crimes)
#     print(reader)
#     for line in reader:
#         year = datetime.datetime.strptime(line['Date'], '%m/%d/%Y %H:%M:%S %p').year
#         if year == 2015:
#             crime_type = line['Primary Type']
#             if crime_type in type_crime_counter.keys():
#                 type_crime_counter[crime_type] += 1
#             else:
#                 type_crime_counter[crime_type] = 0
#
# top_crime = dict(
#     crime='',
#     count=0
# )
# for crime, count in type_crime_counter.items():
#     if top_crime['count'] < count:
#         top_crime['count'] = count
#         top_crime['crime'] = crime
#
# print(top_crime['crime'], type_crime_counter)

# второй вариант:
from collections import Counter

type_crime = []
with open("Crimes.csv", "r") as crimes:  # Открываем наш файл для чтения:
    reader = csv.DictReader(crimes)
    for line in reader:
        year = datetime.datetime.strptime(line['Date'], '%m/%d/%Y %H:%M:%S %p').year
        if year == 2015:
            type_crime.append(line['Primary Type'])

print(Counter(type_crime).most_common(1)[0][0])