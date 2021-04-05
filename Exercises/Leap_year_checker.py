Y = int(input())  # Введите год для проверки
if Y % 4 != 0:
    print('Обычный')
elif Y % 100 == 0 and Y % 400 != 0:
    print('Обычный')
else:
    print('Високосный')