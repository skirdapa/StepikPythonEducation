"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
"""
# Первый вариант
# lst = []
# with open('file.txt', 'r') as file:
#     for line in file:
#         lst.append(line.strip())
#
# print(lst)
# lst.reverse()
# print(lst)
#
# with open('file_2.txt', 'w') as file:
#     for line in lst:
#         file.write(line + '\n')
# Еще варианты:
lines = open("file.txt").readlines()
print(lines)
print(lines[::-1])
print(reversed(lines))
with open("file_2.txt", "w") as file:
    file.writelines(reversed(lines))
