A = int(input('Рекомендуется спать минимум: '))
B = int(input('Но не более: '))
H = int(input('Ана спит: '))
if H < A:
    print('Недосып')
elif A <= H <= B:
    print('Это нормально')
else:
    print('Пересып')
