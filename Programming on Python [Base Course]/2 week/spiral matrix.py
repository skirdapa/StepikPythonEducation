"""
Выведите таблицу размером n×n, заполненную числами от 1 до n ** 2
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
"""
n = int(input())
matrix = [[0 for j in range(n)] for i in range(n)]
# print(matrix)
cnt = 0
up_rows = 0
down_rows = 0
left_cols = 0
right_cols = 0
while cnt < n ** 2:
    # заполняет верхний ряд слева направо
    for i in range(0 + left_cols, n - right_cols):
        cnt += 1
        matrix[0 + up_rows][i] = cnt
    up_rows += 1  # запоминаем что заполнили ряд сверху
    # заполняем правый столбец сверху вниз
    for i in range(0 + up_rows, n - down_rows):
        cnt += 1
        matrix[i][n - 1 - right_cols] = cnt
    right_cols += 1  # запоминаем что заполнили ряд справа
    # заполняем нижний ряд справа налево
    for i in range(n - right_cols - 1, 0 + left_cols - 1, -1):
        cnt += 1
        matrix[n - 1 - down_rows][i] = cnt
    down_rows += 1  # Запоминаем что заполнили ряд снизу
    # заполняем левый столбец снизу вверх
    for i in range(n - down_rows - 1, 0 + up_rows - 1, -1):
        cnt += 1
        matrix[i][0 + left_cols] = cnt
    left_cols += 1  # Запоминаем что заполнили столбец слева

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end='\t')
    print()
