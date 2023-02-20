import requests
from bs4 import BeautifulSoup as BS

def my_menu_city (numeric):
    if (int(numeric) >= 0 and int(numeric) <=26) or int(numeric)==77:
        return int(numeric)
    if int(numeric) == 99:
      exit()
    else:
        print('Choice is out of range!')

def my_menu2 (numeric):
    if (int(numeric) >= 1 and int(numeric) <=11) or int(numeric) == 77:
        return int(numeric)
    elif int(numeric) == '99':
        quit()
    else:
        print('Choice is out of range!')
def my_name_pokazatel (numeric):
    if int(numeric) == 1:
        return ('T воздуха(ср)')
    if int(numeric) == 2:
        return ('T воздуха(max)')
    if int(numeric) == 3:
        return ('T воздуха(min)')
    if int(numeric) == 4:
        return ('TповерхностиMin')
    if int(numeric) == 5:
        return ('MinTнадЗемлей)')
    if int(numeric) == 6:
        return ('Влажность(ср)')
    if int(numeric) == 7:
        return ('Влажность (min)')
    if int(numeric) == 8:
        return ('SpeedВетра(ср)')
    if int(numeric) == 9:
        return ('SpeedВетра(max)')
    if int(numeric) == 10:
        return ('Осадки (мм) ')
    if int(numeric) == 11:
        return ('Солнеч.Day')
    if int(numeric) == 77 or numeric=='77':
        return ('ВСЕ показатели')

#Функция печати на экран
def my_print(choose1,choose2):
    if choose1 == '77' and len(choose2) > 2 and choose2 != '77':
        # Если выбрано меню 77 города все
        user_choice_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                           25]
        some_list = list(choose2.split(' '))  # закидіваем в спсиок через пробел
        for num in some_list[::-1]:
            for num1 in user_choice_lst:
                print('Твой город - ', my_list_new[my_menu_city(num1)][0], 'Значение показателя',
                  my_name_pokazatel(num), " ", my_list_new[my_menu_city(num1)][my_menu2(num)])
        # Если показатель 77 и город один
    elif choose2 == '77' and len(choose1) >2 and choose1 != '77':
        user_choice2_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        some_list = list(choose1.split(' '))  # закидіваем в спсиок через пробел
        for num in some_list[::-1]:
            for num1 in user_choice2_lst:
                print('Твой город - ', my_list_new[my_menu_city(num)][0], 'Значение показателя',
                      my_name_pokazatel(num1), " ", my_list_new[my_menu_city(num)][my_menu2(num1)])
    if choose1 == '77' and len(choose2)<=2 and choose2 != '77':
    # Если выбрано меню 77 города все
        user_choice_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                               25]
        for num1 in user_choice_lst:
            print('Твой город - ', my_list_new[my_menu_city(num1)][0],'Значение показателя',
                      my_name_pokazatel(choose2), " ",my_list_new[my_menu_city(num1)][my_menu2(choose2)])
        # Если показатель 77 и город один
    elif choose2 == '77' and len(choose1) <= 2 and choose1!='77':
        user_choice2_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        print('Твой город - ', my_list_new[my_menu_city(choose1)][0])
        for num1 in user_choice2_lst:
            print('Значение показателей', my_name_pokazatel(num1), " ",
                  my_list_new[my_menu_city(choose1)][my_menu2(num1)])
    elif choose2 == '77' and choose1 == '77':
        user_choice_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        user_choice2_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        for num1 in user_choice_lst:
            print('Твой город - ', my_list_new[num1][0])
            for num2 in user_choice2_lst:
                print('Значение показателя', my_name_pokazatel(int(num2)), " ",my_list_new[num1][int(num2)])
    # Если несколько городов и один показатель
    elif (len(choose1)>2 and len(choose2)<=2) and int(choose2) != 77:
        some_list = list(choose1.split(' ')) # закидіваем в спсиок через пробел
        for num in some_list[::-1]:
             print('Твой город - ' ,my_list_new[my_menu_city(num)][0])
             print('Значение показателя', my_name_pokazatel(choose2), " ",
              my_list_new[my_menu_city(num)][my_menu2(choose2)])
    # Если один город и несколько показателей через пробел
    elif len(choose2)>2 and len(choose1)<=2 and int(choose1) != 77:
        some_list = list(choose2.split(' ')) # закидіваем в спсиок через пробел
        print('Твой город - ', my_list_new[my_menu_city(choose1)][0])
        for num in some_list[::-1]:
             print('Значение показателя', my_name_pokazatel(num), " ",
             my_list_new[my_menu_city(choose1)][my_menu2(num)])
    # # Если несколько городов и несколько показателей через пробел
    elif len(choose2) > 2 and len(choose1) >2:
        some_list1 = list(choose1.split(' '))  # закидіваем в спсиок через пробел
        some_list2 = list(choose2.split(' '))
        for num1 in some_list1[::-1]:
            print('Твой город - ', my_list_new[my_menu_city(num1)][0])
            for num2 in some_list2[::-1]:
                print('Значение показателя', my_name_pokazatel(num2), " ",
                  my_list_new[my_menu_city(num1)][my_menu2(num2)])
    elif len(choose2) <= 2 and len(choose1) <=2 and (choose2 != 77 or choose1 != 77):
          print('Твой город - ' ,my_list_new[my_menu_city(choose1)][0])
          print('Значение показателя',my_name_pokazatel(choose2)," ", my_list_new[my_menu_city(choose1)][my_menu2(choose2)])

    print('Введите новый запрос ниже:')

#======================= Идет парсер страницы ================================

print('Идет обработка запроса и запуск программы')
my_url='https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
full_page=requests.get(my_url,headers=headers)
soup=BS(full_page.content,'html.parser')
rate=soup.find_all('td')

my_list_temp=[]
my_list_new=[]
#my_list = []
for my_list in rate:
    my_list_temp.append(my_list.text)
#Всего 26 городов, 11 параметров
my_list_temp2=[]
#Формируем список в списке
for i in range(0,len(my_list_temp),12):
    for j in range(0,12):
        my_list_temp2.append(my_list_temp[i+j])
    my_list_new.append(my_list_temp2)
    my_list_temp2=[]
#============= Парсер закончился ===========================

#============== Формируем меню ввода ========================
while True:
    user_choice =input(
    "\n0.Heltermaa       	        1.Jõgeva             	2.Jõhvi            	3.Kihnu		4.Kunda"
    "\n5.Kuressaare linn	        6.Kuusiku		       	7.Lääne-Nigula		8.Narva		9.Pakri"
    "\n10.Pärnu		    	    11.Ristna		    	12.Roomassaare		13.Ruhnu	14.Sõrve"
    "\n15.Tallinn-Harku		    16.Tartu-Tõravere   	17.Tiirikoja		18.Tooma	19.Türi"
    "\n20.Valga			        21.Viljandi			    22.Vilsandi			23.Virtsu	24.Võru"
    "\n25.Väike-Maarja		        77.<<All>>		        99.<<EXIT>>"
    "\nВыберите номер города по которому смотрим данные (можно указате несколько через пробел Пример:1 18 3 или 77-Все) --->")


    user_choice2 = input(
    "\n1.T воздуха(ср)          2.T воздуха(max)            3.T воздуха(min)"
    "\n4.TповерхностиMin        5.MinTнадЗемлей)            6.Влажность(ср)!"
    "\n7.Влажность (min)!       8.SpeedВетра(ср)            9.SpeedВетра(max)"
    "\n10.Осадки (мм)            11.Солнеч.Day               77.<<ALL>>          99.Выход"
    "\nВыберите номер показателя (Можно несколько через пробел 3 5 6 или 77-Все)--->")
    # вызываем функцию передачи города и показателя на печать

    my_print(user_choice,user_choice2)
# Делаем вывод: один город и один показатель, два города и один показатель, два показателя и один город
# Делаем еще если 77 стоить Все. Если 77 и несколько показателей
    # #Если город 77 и показатель один


print('Good bye')