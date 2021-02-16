'''
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''

var2 = b'attribute'
var3 = b'класс'
var4 = b'функция'
var5 = b'type'


'''
    var3 = b'класс'
           ^
SyntaxError: bytes can only contain ASCII literal characters.

    var4 = b'функция'
           ^
SyntaxError: bytes can only contain ASCII literal characters.

Синтаксическая ошибка так как кириллицы нет в кодировке ASCII. Байты могут только содержать символы из таблицы ASCII.

'''