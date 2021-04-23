import os
import os.path
import shutil
py_dir = []
with open("py_finder.txt", "w") as out:
    # Метод os.walk обходит каталог и возвращает кортеж (имя текущей директории, [список папок в ней], [список файлов])
    for current_dir, list_dir, list_file in os.walk("main"):
        # print(current_dir, list_dir, list_file)
        for file in list_file:
            if file[-3:] == '.py':  # Проверяем что расширение файла .py, можно использовать метод .endwith
                py_dir.append(current_dir)
                break

print(*sorted(py_dir), sep='\n')

with open('file_with_py.txt', 'w') as file:
    file.writelines("\n".join(py_dir))
