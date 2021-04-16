"""
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:

y больше или равно x
y делится нацело на 5
Формат того, что ожидается от вас в качестве ответа:

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return "I don't know :("

"""


# циклом
def closest_mod_5(x):
    while x % 5 != 0:
        x += 1
    return x


# рекурсией
def closest_mod_5_rec(x):
    return x if x % 5 == 0 else closest_mod_5_rec(x + 1)


# матформулой
def closest_mod_5_formula(x):
    return (x + 4) // 5 * 5


x = int(input())
print(closest_mod_5(x))
print(closest_mod_5_rec(x))
print(closest_mod_5_formula(x))
