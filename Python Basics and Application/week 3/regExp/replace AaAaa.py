"""
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

Примечание:
Обратите внимание на параметр count у функции sub.
Sample Input:

There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA
Sample Output:

There’ll be no more "argh"
argh AaAaAaA
"""
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\b[aA]+\b', 'argh', line, count=1))
    # И второй вариант с флагом игнорирования регистра
    # print(re.sub(r'\ba+\b', 'argh', line, count=1, flags=re.IGNORECASE))
