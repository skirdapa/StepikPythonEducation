#  Формула Герона для вычисления площади треугольника по трем сторонам

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print(S)
