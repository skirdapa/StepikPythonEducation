"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
"""
import json

json_string = input()
# json_string = '''[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []},
# {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'''
# json_string = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
json_children = json.loads(json_string)
# print(json_children)

# составим словарь c ключом родителем и множеством детей
json_parents = {}


def get_children(human_parent, grand_parent):
    # Если человека еще нет в нашем списке то добавляем его c пустым множеством детей
    if human_parent not in json_parents.keys():
        json_parents[human_parent] = set()
    # Проходим по JSON-у в поисках родителя:
    for child in json_children:
        # Если есть такой родитель
        if grand_parent in child['parents']:
            # То добавляем ребенка человеку
            json_parents[human_parent].add(child['name'])
            # и идем по ребенку
            get_children(human_parent, child['name'])


for child in json_children:
    get_children(child['name'], child['name'])

for human in sorted(json_parents):
    print(human, len(json_parents[human]) + 1, sep=' : ')



