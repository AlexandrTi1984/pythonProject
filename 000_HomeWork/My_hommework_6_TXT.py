"""""""""
Написать программу которая открывает текстовый файл и считает следующее:
1. Общее кол-во слов
2. Кол-во уникальных (разных)
Не влияет на уникальность:
Заглавные и прописные буквы
Знаки препинания: ',' '.' '!' '?'
Сохраняет кол-ва в отдельный файл.
Выписывает все уникальные слова в алфавитном порядке.
"""""""""

import os


with open('Example_book.txt', 'r', encoding='UTF8') as file:
    file_content = file.read().lower()    #Все в нижний регистр, т.к строка
    my_string = file_content.split()
#    my_string.sort()
for i in range(len(my_string)):
    my_string_change=str(my_string[i])
    my_len = len(str(my_string[i]))
 #Если последний символ точка, запятая ... убираем его и записываем в список
    if my_string_change[my_len-1:my_len] in ('»,.?!;:'):    #Если два символа подряд, можно 2-3 раза проверить !!!
        my_string[i]=my_string_change[0:my_len-1]
# Если первый символ «, вырезаем его
    if my_string_change[0] in ('«"'):
        my_string[i] = my_string_change[1:my_len]
my_string_unikalnie=list(set(my_string)) # убрали дубликаты
my_string_unikalnie.sort()
# переводим в str
my_printstring1=('Количество слов составляет ' + str(len(my_string)) + ' штук')
my_printstring2=('Количество уникальных слов составляет ' + str(len(my_string_unikalnie)) + ' штук')

#Check if file exists, then delete it:  https://www.w3schools.com/python/python_file_remove.asp
# if os.path.exists("My_txt.txt"):
#   os.remove("My_txt.txt")
#  # print("The file exist")
# else:
#   print("The file does not exist")

with open ('1-My_txt.txt', 'w',encoding='UTF8') as file:
    file.write(str(my_printstring1) + '\n')
    file.write(str(my_printstring2) + '\n'+'\n')
    for i in range(len(my_string_unikalnie)):
        write_string=str(my_string_unikalnie[i])
        file.write(write_string + '\n')

