from random import random


class RandomIterator:

    # Добавим переменную отвечающую за количество итераций при инициализации
    def __init__(self, k):
        self.k = k  # Максимальное количество итераций
        self.i = 0  # Количество пройденных итераций

    # Что бы применять к объекту функцию next(x) внутри него должно быть определена функция __next__
    def __next__(self):
        # Добавляем условие что итераций не больше заданного
        if self.i < self.k:
            self.i += 1
            return random()
        else:  # Иначе бросаем исключение
            raise StopIteration

    # Что бы по нашему объекту можно было итерироваться, нужно объявить метод __iter__
    def __iter__(self):
        return self


# x = RandomIterator(3)
# print(next(x))  # next(x) ~ x.__next__(),  x -- итератор
# print(next(x))
# print(next(x))

for i in RandomIterator(10):
    print(i)
