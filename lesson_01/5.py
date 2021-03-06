'''
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
результаты из байтовового в строковый тип на кириллице.
'''

import subprocess

ping_resource = ['yandex.ru', 'youtube.com']
for ping_now in ping_resource:
    args = ['ping', ping_now]
    ping_process = subprocess.Popen(args, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i < 3:
            # print(line)
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            print('= ' * 25)
            break

# Вариант 2


# ping_resurs = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
#
# for ping_now in ping_resurs:
#
#     ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)
#
#     i = 0
#
#     for line in ping_process.stdout:
#
#         if i < 3:
#             # print(line)
#             line = line.decode('cp866').encode('utf-8')
#             print(line.decode('utf-8'))
#             i += 1
#         else:
#             print('= ' * 25)
#             break
