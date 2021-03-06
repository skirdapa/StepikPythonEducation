"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""
n = int(input())
table = {}
for _ in range(n):
    line = input().split(';')
    # Добавляем команды в таблицу, если их еще нет
    if line[0] not in table.keys():
        table[line[0]] = [0, 0, 0, 0, 0]  # key = название команды, value [игр, побед, ничьих, поражений, очков
        # print('Добавили первую команду', table)
    if line[2] not in table.keys():
        table[line[2]] = [0, 0, 0, 0, 0]  # key = название команды, value [игр, побед, ничьих, поражений, очков
        # print('Добавили вторую команду', table)

    # Прибавляем командам + 1 игру
    table[line[0]][0] += 1
    table[line[2]][0] += 1

    # Заполняем результаты в таблицу
    # В случае победы первой команды
    if int(line[1]) > int(line[3]):
        # print('Первая команда победила')
        table[line[0]][1] += 1  # Первой команде добавляем одну победу
        table[line[0]][4] += 3  # и три очка
        table[line[2]][3] += 1  # Второй команде добавляем поражение
        # print(table)
    # В случае победы второй команды
    elif int(line[1]) < int(line[3]):
        # print('Вторая команда победила')
        table[line[2]][1] += 1  # Второй команде добавляем одну победу
        table[line[2]][4] += 3  # и три очка
        table[line[0]][3] += 1  # Первой команде добавляем поражение
        # print(table)
    # В случае ничьей
    else:
        # print('Ничья')
        table[line[2]][2] += 1  # Второй команде добавляем одну ничью
        table[line[2]][4] += 1  # и одно очко
        table[line[0]][2] += 1  # Первой команде добавляем одну ничью
        table[line[0]][4] += 1  # и одно очко
        # print(table)


# Выводим результаты
for team, results in table.items():  # цикл по словарю где team - ключ, название команды, results - значение, список
    print(team + ':', *results)



