"""
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz"
у вас появляется ссылка "download your dataset". Используйте эту ссылку для того,
чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу,
используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится,
надо отправить в качестве ответа на эту задачу.
"""
with open('dataset_3363_2.txt', 'r') as dataset:
    archive_string = dataset.readline().strip()

print(archive_string)

unpacking_string = ''
symbol = ''
count_symbol = ''
i = 0
while i < len(archive_string):
    if not archive_string[i].isdigit():
        symbol = archive_string[i]
        i += 1
    else:
        while archive_string[i].isdigit():
            count_symbol += archive_string[i]
            i += 1
            if i == len(archive_string):
                break
        print(symbol, count_symbol)
        unpacking_string += symbol * int(count_symbol)
        count_symbol = ''

print(unpacking_string)

with open('rez_file.txt', 'w') as rez_file:
    rez_file.write(unpacking_string)

