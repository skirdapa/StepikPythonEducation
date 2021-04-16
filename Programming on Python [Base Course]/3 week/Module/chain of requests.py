"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
"""
import requests

with open('first_url.txt', 'r') as first_link:
    another_link = first_link.read().strip()

first_word = ''
i = 0
while True:
    my_file = requests.get(another_link).text.strip()
    i += 1
    print(my_file, i)
    if my_file.split()[0] == 'We':
        print(requests.get(another_link).text)
        break
    another_link = 'https://stepic.org/media/attachments/course67/3.6.3/' + my_file
