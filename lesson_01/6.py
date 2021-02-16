'''
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''
import locale

resurs_string = ['сетевое программирование', 'сокет', 'декоратор']

def_coding = locale.getpreferredencoding()
print(def_coding)

# Создаем файл и заносим в него данные
with open('test_file.txt', 'w+') as f_n:
    for i in resurs_string:
        f_n.write(i + '\n')
    f_n.close()
print(f_n)  # печатаем объект файла, что бы узнать его кодировку

# Читаем из файла
with open('test_file.txt', 'r', encoding='utf-8') as f_n:
    for i in f_n:
        print(i, end='')
