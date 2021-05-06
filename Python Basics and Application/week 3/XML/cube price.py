"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:

4 3 1
"""
from lxml import etree


# tag
# attrib

# cube_string = input()
cube_string = '''
<cube color="blue">
    <cube color="red">
        <cube color="green">
            <cube color="green">
                <cube color="green">
                    <cube color="blue">
                    </cube>
                    <cube color="green">
                    </cube>
                    <cube color="red">
                    </cube>
                </cube>
            </cube>
        </cube>
    </cube>
    <cube color="red">
        <cube color="blue">
        </cube>
    </cube>
</cube>
'''
cube_xml = etree.fromstring(cube_string)

print(cube_xml)

color_count = {}


def get_child(root, depth):
    depth += 1
    if root.attrib['color'] not in color_count:
        color_count[root.attrib['color']] = 0
    color_count[root.attrib['color']] += depth
    print(depth, root.attrib['color'])
    for child in root:
        get_child(child, depth)

get_child(cube_xml, 0)
print(color_count)

print(color_count['red'], color_count['green'], color_count['blue'])


