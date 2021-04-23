# Реализуем свой способ итерации обектов, по два сразу
class DoubleElementsListIterator:  # Объект итератор, есть функция __next__
    # При инициализации передаем лист
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    # При каждой итерации выдаем два следующих элемента
    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration


# Создаем свой класс, который при итерировании будет пользоваться вышезаданным поведением
class MyList(list):  # Итерируемый объект, есть функция __iter__
    def __iter__(self):
        return DoubleElementsListIterator(self)


for pair in MyList([1, 2, 3, 4, 5, 6, 7, 8]):
    print(pair)
