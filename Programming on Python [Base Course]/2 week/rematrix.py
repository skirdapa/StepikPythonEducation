"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции cls, j равен сумме элементов
первой матрицы на позициях (cls-1, j), (cls+1, j), (cls, j-1), (cls, j+1). У крайних символов соседний элемент
находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""
i = 0
lst = []
myStr = ''
while True:  # Заполняем наш массив
    myStr = input()
    if myStr == 'end':
        break
    lst.append(myStr.split())
    i += 1

# print(lst)

n = len(lst)
m = len(lst[0])
for i in range(n):  # Превращаем строки в инты, чтоб потом не раздувать строку подсчёта
    for j in range(m):
        lst[i][j] = int(lst[i][j])

# print(lst)
# Преобразуем наш массив и выводим
for i in range(n):
    for j in range(m):
        i_up = i - 1
        i_down = i + 1
        j_left = j - 1
        j_right = j + 1
        if i_up < 0:
            i_up = n - 1
        if i_down > n - 1:
            i_down = 0
        if j_left < 0:
            j_left = m - 1
        if j_right > m - 1:
            j_right = 0
        print(lst[i_up][j] + lst[i_down][j] + lst[i][j_left] + lst[i][j_right], end=' ')
    print()




