"""
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить
неположительное целое число бросалось исключение NonPositiveError и число не добавлялось,
а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.

Примечание:
Положительными считаются числа, строго большие нуля.
"""


class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError(str(x) + " is not positive number")


p_list = PositiveList()
print(p_list)
p_list.append(1)
print(p_list)
p_list.append(0)
print(p_list)
p_list.append(-1)
print(p_list)
