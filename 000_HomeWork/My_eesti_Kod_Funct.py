def gender_pol (pol_gender):
    # Проверка пола первой цифры
    if int(pol_gender) == 0 or int(pol_gender) == 9:
        print("Не верный код, ошибка в 1 символе")
        quit()

    if int(pol_gender) % 2 == 0:
        My_pol = 'Женщина'
    else:
         My_pol = 'Мужчина'
    return  My_pol

def my_date_birthday (my_d, my_m, my_era,my_y): # передача день, месяц, год
    my_date_send=''
    # Проверка даты на 31
    if int(my_d) > 31:
        print("Не верный код, ошибка в 6-7 символе")
        quit()
        # Проверка месяца
    if  int(my_m) > 12:
      print("Не верный код, ошибка в 4-5 символе")
      quit()

    if int(my_era)==1 or int(my_era)==2:
        my_date_send= my_d +'.'+ my_m + '.'+'18'+str(my_y)
    if int(my_era)==3 or int(my_era)==4:
        my_date_send=my_d +'.'+ my_m + '.'+'19'+str(my_y)
    if int(my_era)==5 or int(my_era)==6:
        my_date_send=my_d +'.'+ my_m + '.'+'20'+str(my_y)
    if int(my_era)==7 or int(my_era)==8:
        my_date_send=my_d +'.'+ my_m + '.'+'21'+str(my_y)
    return my_date_send

def bolnica_name (my_era, my_y, my_value):
    my_date_send = ''

    if int(my_era) == 1 or int(my_era) == 2:
        my_date_send = '18' + str(my_y)
    if int(my_era) == 3 or int(my_era) == 4:
        my_date_send = '19' + str(my_y)
    if int(my_era) == 5 or int(my_era) == 6:
        my_date_send = '20' + str(my_y)
    if int(my_era) == 7 or int(my_era) == 8:
        my_date_send = '21' + str(my_y)

    if int(my_date_send)<2013:
        print('Рожден до 2013 года')
    else:
        print('Рожден после 2013 года')

    lst1=[1,11,21,151,161,221,271,371,421,471,491,521,571,601,651]
    lst2=[10,19,150,160,220,270,370,420,470,490,520,570,600,650,700]
    lst3=['Больница Курессааре','Наистеклиник Тартуского университета',
      'Восточно-Таллиннская центральная больница родильный дом Пелгулинна Таллинн',
      'Больница Кейла','Больница Рапла, больница Локса, больница Хийумаа (Кярдла)',
      'Восточно-Вируская центральная больница (Кохтла-Ярве, бывший Йыхви)',
      'больница Маарьямыйса (Тарту), больница Йыгева', 'Нарвская больница',
      'Красивая больница','Больница Хаапсалу','Больница Ярвамаа (платная)',
      'Больница Раквере, Убей больницу','больница Валга','больница Вильянди',
      'Южно-эстонская больница (Выру), Пылвская больница']

#Проверка есть не верно составлен список
    if len(lst1)!=len(lst2) or len(lst2)!=len(lst3):
         print('Списки разные длинны')
         quit()
    for i in range(len(lst1)):
     if int(my_value)>lst1[i] and int(my_value)<lst2[i]:
         return lst3[i]

def chek_key_1_2 (control_number):
    lst4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    lst5 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    sum1 = 0
    sum2 = 0
    key1= False
    key2 = False
    for i in range(10):
        sum1 = sum1 + lst4[i] * int(control_number)
        sum2 = sum2 + lst5[i] * int(control_number)
    # Если 10 то проверяем на 0.
    # Проверка на ключ
    if sum1 - (sum1 // 11) * 11 == int(control_number):
        key1=True
    if sum1 - (sum1 // 11) * 11 == 10 and int(control_number) == 0:
        key1=True
    if sum2 - (sum2 // 11) * 11 == int(control_number):
        key2=True
    if sum2 - (sum2 // 11) * 11 == 10 and int(control_number) == 0:
        key2 = True
    if key1==True and key2==True:
        return 'Ваш код корректен (проверка прошла по двум проверкам)'
    if key1==True and key2==False:
        return 'Ваш код корректен (Первая проверка прошла, вторая - нет)'
    if key1==False and key2==True:
        return 'Ваш код корректен (Первая проверка не прошла, вторая - прошла)'
    if key1==False and key2==False:
        return 'Ваш код не корректен (Первая проверка не прошла, вторая - не прошла)'