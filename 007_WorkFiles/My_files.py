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

with open (r'My_txt2','r') as file:  #автоматом закріваем файл и соединение
   # data=file.read() # читает количесто символов
   data=file.readlines() #создает список с \n перенос строки
   print(data)
   print(len(data))
   print(type(data))
    # data=file.read() # читает количесто символов
    # print(data.upper()) #доходит до конца, обратно не возвращается
#     print(file.closed)
#
# print(file.closed)
