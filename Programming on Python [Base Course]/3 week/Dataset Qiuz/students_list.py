"""
Имеется файл с данными по успеваемости абитуриентов.
Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает
его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и
добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику
и одной строкой со средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
"""
students = []
with open('students_mark.txt', 'r') as marks:
    for line in marks:
        students.append(line.strip().split(';'))

print(students)

with open('students_avg_mark.txt', 'w') as mark_file:
    avg_mark = [0, 0, 0]
    for student in students:
        avg_mark[0] += int(student[1])
        avg_mark[1] += int(student[2])
        avg_mark[2] += int(student[3])
        print(student[0], (int(student[1]) + int(student[2]) + int(student[3]))/3)
        mark_file.write(str((int(student[1]) + int(student[2]) + int(student[3]))/3) + '\n')
    print(avg_mark[0]/len(students), avg_mark[1]/len(students), avg_mark[2]/len(students))
    mark_file.write(str(avg_mark[0]/len(students)) + ' ' + str(avg_mark[1]/len(students)) + ' '
                    + str(avg_mark[2]/len(students)))

