"""
Сначала в качестве аргументов функции идут позиционные аргументы,
потом могут идти позиционные аргументы содержащие значения по умолчанию,
далее может идти произвольное количество неименованных аргементов
или именнованных.
При объялении функции указать произвольное количество неименованных аргументов можно с помощью записи вида:

def myFunc(*arg):
    pass

,где *arg - arguments - список или кортеж (list or tupple, [a, b, c], (a, b, c))

При объялении функции указать произвольное количество именованных аргументов можно с помощью записи вида:

def myFunc(**kwarg):
    pass

,где **kwargs - key words arguments - словать (dict, {a: 1, b: 2})

при вызове функции передать аргументы из списка, кортежа, множества, словаря можно так же

Рассмотрим примеры:
"""


def printab(a, b, c=10, *args, **kwargs):
    print('positional argument a: ', a)
    print('positional argument b: ', b)
    print('positional argument c: ', c)
    print('additional not named arg:')
    for arg in args:
        print(arg)
    print('additional named arg:')
    for arg in kwargs:
        print('key: ', arg, ' value: ', kwargs[arg])


abc_list = [1, 2, 3, 4, 5, 6]
abc_dict = dict(
    e=5,
    d=7,
    f=1111
)
abc_set = {1, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7}

printab(1, 2)

printab(10, 11, 12, 13, 14, d=111, asd=3, werwewe=234)
printab(1, 2, *abc_list)
printab(*abc_list, **abc_dict)
printab(1, 2, *abc_list, **abc_dict)
printab(*abc_set)
