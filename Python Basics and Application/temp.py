my_set = set()
my_dict = dict(
    a=[],
    b=['c', 'd'],
    e=['a', 'b', 'c', 'd']
)

my_set.add('a')
# my_set.add(*my_dict['a'])
my_set.add('b')
my_set.update(set(my_dict['b']))
print(my_set)

if my_dict['a']:
    print('a')
if my_dict['b']:
    print('b')
