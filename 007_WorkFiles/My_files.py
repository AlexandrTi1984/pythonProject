import antigravity
# r     - read
# a     - append
#w      - write
#x      - creare
#r +    - read and write
# #file = open('My_txt2','r',encoding='UTF8')
# file = open('My_txt','r')
# print(file.name)
# print(file.mode)
# print(file.encoding)
# print(file.close())
# file.close()   #файл закріть
# print(file.close())

# cd ../  возврат на папку назад
#Absolute Path  абсолютный пункт
#C:\Users\baran\PycharmProjects\pythonProject\txt\My_txt.txt

#relative     от оносительныйпуект
#txt/My_txt

#with open (r'My_txt2','r') as file:  #автоматом закріваем файл и соединение
   # data=file.read() # читает количесто символов
  # data=file.readlines() #создает список с \n перенос строки

   # chunk=1000
   # data=file.read(chunk)
   # while len(data):
   #    print(data)
   #    data = file.read(chunk)

  # data=file.readline()  # читает строчное чтение по параграфу (работа с отдельніми обзацами)
# print(data)
# print(len(data))
# print(type(data))
    # data=file.read() # читает количесто символов
#     # print(data.upper()) #доходит до конца, обратно не возвращается
# #     print(file.closed)
# import datetime
# dt=datetime.date.today()
#
# # print(file.closed)
# #with open (r'My_txt22.txt','w',encoding='UTF8') as file:  #создает файл если его нет
# #with open(f'My_txt22{dt}.txt', 'w', encoding='UTF8') as file:  # создает файл с текущей датой
# # with open ('My_txt2.txt', 'r', encoding='UTF8') as read_file:
# #    data=read_file.read()
# #    with open(f'My_txt22.txt', 'w', encoding='UTF8') as file:  # создает файл c добавлением, дописанием текста в конец
# #       file.write(data.upper())
# # with open('My_txt123.txt', 'x', encoding='UTF8') as  file: # для создания файла, повторно создать нельзя для первичного создания с проверкой о наличии такого файла
# #    file.write('Hello')
# # with open('My_txt123.txt', 'x',
# #       encoding='UTF8') as file:  # для создания файла, повторно создать нельзя для первичного создания с проверкой о наличии такого файла
# #       file.write('Hello')
#
# #взять файл откріть, поредактировать, записать.
#
#
# with open('My_txt1234.txt', 'r+',encoding='UTF8') as file:  # для создания файла, повторно создать нельзя для первичного создания с проверкой о наличии такого файла
#       data = file.read()
#       print(data)
#       file.write(data.upper())
#
#    # data=file.read()
#    # print(len(data))
#  #  file.seek(0)
#  #   file.write('Hello яяя\n') #записівает и перезаписывает   перенос строки
#  # #  file.seek(0)
#  #   file.write('jjjjj Александр') #записівает и перезаписывает
#  #   file.write(str(77777))  # записівает и перезаписывает
#
#    # file.seek(0)  # вовзрат на позицию, на нулевой индекс, начало файла
#    # data=file.read()
#    # print(len(data))

with open('python.png','rb') as my_file:
  #    data=my_file.read()
      with open('python1.png','wb') as wfile:
         data = my_file.read()
         while len(data)>0:
             wfile.write(data)
             data = my_file.read(4096)

