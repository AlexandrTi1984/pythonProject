import os

def my_function_file_copy(file_2,filepath):
    #Если нет директории то создаем новую + создаем пути и перемещаем файлы
    if file_2 in ('.jpg','.png'):
        if os.path.isdir('my_file\picture') == False:
            os.makedirs('my_file\picture')
        os.replace(str(os.path.join('my_file\\', filepath)), str(os.path.join('my_file\picture\\', filepath)))
    elif my_lst2[1] in ('.xlsx','.xls','.docx','.txt','.pdf'):
         if os.path.isdir('my_file\Documents') == False:
             os.makedirs('my_file\Documents')
         os.replace(str(os.path.join('my_file\\', filepath)), str(os.path.join('my_file\Documents\\', filepath)))
    elif my_lst2[1] in ('.mp3','.wav'):
         if os.path.isdir('my_file\Music') == False:
             os.makedirs('my_file\Music')
         os.replace(str(os.path.join('my_file\\', filepath)), str(os.path.join('my_file\Music\\', filepath)))
    elif my_lst2[1] in ('.avi','.mp4'):
         if os.path.isdir('my_file\Video') == False:
             os.makedirs('my_file\Video')
         os.replace(str(os.path.join('my_file\\', filepath)), str(os.path.join('my_file\Video\\', filepath)))
    return

#Старт самой программы
my_list = list(os.listdir('my_file'))
#Отделяет расширение файла
for list_file_name in my_list:
    my_lst2=os.path.splitext(list_file_name)
    my_function_file_copy(my_lst2[1],list_file_name) #расширение и название файла
