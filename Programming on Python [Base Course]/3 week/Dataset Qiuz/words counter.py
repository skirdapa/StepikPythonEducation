"""
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.
"""
words = []
with open('book.txt', 'r') as book:  # Открываем файл и читаем его
    for line in book:  # Читаем построчно
        words += line.strip().lower().split()  # Удаляем служебыные символы, приводим к нижнему регистру, разбиваем

count_words = {}

print(words)
words = sorted(words)
print(words)

for word in set(words):  # берем слова из множества слов, множества содержат только уникальные элементы
    count_words[word] = words.count(word)  # Считаем сколько слов содержтся в книге

print(count_words)
print(sorted(count_words.values(), reverse=True))

count = 0
popular_words = ''
for word in count_words:  # Ищем самое популярное слово
    if count_words[word] > count:
        count = count_words[word]
        popular_words = word
    elif count_words[word] == count:  # Если слова одинаково популярны, берем первое по алфавиту
        if word > popular_words:
            popular_words = word

print(popular_words, count)
