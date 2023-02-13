import os
import time

#print(dir(os))
# # print(os.getcwd()) #текущий католог
# # #смена пути запуска библиотек
# # os.chdir('../')
# # # print(os.getcwd())
# # # open(os.getcwd() +'/sample.txt')
# # print(os.listdir()) #список всех файлов
# # print(os.listdir('../')) #список всех файлов
#
# #создать папку только в одной директории
# #os.mkdir('../999_test')
#
# #создать все папки в подкатологе только в одной директории
# #os.makedirs('../999_test/test/nes')
#
# #Запукс через 6 секунд
# #time.sleep(6)
#
# #Удаляет папку
# #os.rmdir('999_test')
# #Удаляет всю цепочку
# #os.removedirs('999_test/test/nes') #может нужно ../
# #можно перемещать и переименовать
# #os.rename('sample.txt', 'sample.txt')
# #os.rename('test.txt','sample.txt')
#
# #удялет файл не  вкорзину, только файл
# # os.remove('sample.txt')
# # os.rmdir('temp') # удаляет директорию
#
# #различнон инфо о файле Через точку смотрим атрибуты
# print(os.stat('sample.txt'))
#
info=os.walk('../') #генератор
print(info)
#
for dirpath, dirnames, filenames in info:
    print('Текушая директория ' + dirpath)
    print('Папки' + str(dirnames))
    print('Файлы' + str(filenames))
    if 'tester.py' in filenames:
        print('*' * 40)
        print(dirpath)
        print('*' * 40)
    print()
#

#переменные среды оттуда данные
# print(os.environ.get('USERNAME'))
# file_path = os.environ.get('HOMEPATH')+'\sample.txt'
# print(file_path)

#соединение путей
file_path=os.path.join('C:\home','\sample.txt')
print(file_path)

#Выделяет последний файл или директорию
print(os.path.basename('/somedir/dir10/sample.txt'))

#Отделяет все от последнего значения
print(os.path.dirname('/somedir/dir10/sample.txt'))

#Разбивает на кортедж
print(os.path.split('/somedir/dir10/sample.txt'))

#Отделяет расширение файла
print(os.path.splitext('/somedir/dir10/sample.txt'))

#Наличие такого пути - Проверка путь к файлу или директории
print(os.path.exists('/somedir/dir10/sample.txt'))

#Является ли директорией \ путь - Проверка (только с существующими)
print(os.path.isdir('sample.txt'))

#Является ли файл - Проверка (только с существующими)
print(os.path.isfile('sample.txt'))

