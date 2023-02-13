import os

my_list=list(os.listdir('my_file'))

#print(my_list)
#Отделяет расширение файла
for i in my_list:
    my_lst2=os.path.splitext(i)
  #  print(my_lst2)
    if my_lst2[1] in ('.jpg','.png'):
       if os.path.isdir('my_file\picture') == False:
           os.makedirs('my_file\picture')
       file_path1 = str(os.path.join('my_file\\',my_lst2[0]+my_lst2[1]))
       file_path2 = str(os.path.join('my_file\picture\\', my_lst2[0]+my_lst2[1]))
       #print(os.path.exists(file_path1))
       os.replace(file_path1,file_path2)
    elif my_lst2[1] in ('.xlsx','.xls','.docx','.txt','.pdf'):
         if os.path.isdir('my_file\Documents') == False:
             os.makedirs('my_file\Documents')
         file_path1 = str(os.path.join('my_file\\', my_lst2[0] + my_lst2[1]))
         file_path2 = str(os.path.join('my_file\Documents\\', my_lst2[0] + my_lst2[1]))
         os.replace(file_path1, file_path2)
    elif my_lst2[1] in ('.mp3','.wav'):
         if os.path.isdir('my_file\Music') == False:
             os.makedirs('my_file\Music')
         file_path1 = str(os.path.join('my_file\\', my_lst2[0] + my_lst2[1]))
         file_path2 = str(os.path.join('my_file\Music\\', my_lst2[0] + my_lst2[1]))
         os.replace(file_path1, file_path2)
    elif my_lst2[1] in ('.avi','.mp4'):
         if os.path.isdir('my_file\Video') == False:
             os.makedirs('my_file\Video')
         file_path1 = str(os.path.join('my_file\\', my_lst2[0] + my_lst2[1]))
         file_path2 = str(os.path.join('my_file\Video\\', my_lst2[0] + my_lst2[1]))
         os.replace(file_path1, file_path2)

    #
    #
    #
    #
    #
    #
    #
    #
    #


