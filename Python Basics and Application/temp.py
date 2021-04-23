*a, = range(5)[1:]
print(a)
a = [i + 1 for i in range(4)]
print(a)
a = [i for i in range(4)]
print(a)
a = [i for i in range(5)][1:]
print(a)
a = list(i + 1 for i in range(4))
print(a)
print(*a)
# class Any:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         for i in self.iterable:
#             if i != 2:
#                 yield i
#
#
# list_a = [1, 2, 3]
# obj = Any(list_a)
# list_b = list(obj)
#
# print(list_a)
# print(obj)
# print(list_b)

# my_set = set()
# my_dict = dict(
#     a=[],
#     b=['c', 'd'],
#     e=['a', 'b', 'c', 'd']
# )
#
# my_set.add('a')
# # my_set.add(*my_dict['a'])
# my_set.add('b')
# my_set.update(set(my_dict['b']))
# print(my_set)
#
# if my_dict['a']:
#     print('a')
# if my_dict['b']:
#     print('b')
