# try:
#     user_input=float(input('Enter number' ))
# except: # обработчик ошибки
#     print('Должно быть число')
# else: # Если нет ошибки віполняется код  Необязательно
#     print(user_input**2)
# finally:# Выполнение кода в любом случае  Необязательно
#     print('Looser2')
# print('Looser')
user_id='38405230460'
while True:
    try:
        #user_id=input('ВВеди ид код ')
        int(user_id) # проверка на число
        if len(user_id) !=11:
            raise Exception
    except ValueError:
        print("Введено не число")
        continue
    except Exception:
        if len(user_id)>11:
            print('Код длинный')
        else:
            print('Код короткий')
        continue
    else:
        print('Ваш код', user_id)
        break

##quit()  заканчиваем программу
#exit ()  заканчиваем программу
# \n разрыв строки

# вырезаем данные из строки и смотрим их
my_Male=user_id[0]
my_year=user_id[1:3]
my_month=user_id[3:5]
my_date=user_id[5:7]
my_bolnica=user_id[7:10]
my_kontol_num=user_id[-1]
print(my_Male,my_year,my_month, my_date, my_bolnica,my_kontol_num)


# Проверка пола первой цифры
if  int(my_Male) == 0 or int(my_Male) > 9 :
    print("Не верный код, ошибка в 1 символе")
    quit()
# Проверка месяца
if  int(my_month) > 12:
    print("Не верный код, ошибка в 4-5 символе")
    quit()
# Проверка даты на 31
if  int(my_date) >31:
    print("Не верный код, ошибка в 6-7 символе")
    quit()
# Проверка года

if int(my_Male) %2 == 0:
    My_pol='Woman'
 #   print('Woman')
else:
 #   print('Man')
    My_pol = 'Man'
#Добавляем год к нашему году
if int(my_Male)==1 or int(my_Male)==2:
    my_year='18'+str(my_year)
if int(my_Male)==3 or int(my_Male)==4:
    my_year='19'+str(my_year)
if int(my_Male)==5 or int(my_Male)==6:
    my_year='20'+str(my_year)
if int(my_Male)==7 or int(my_Male)==8:
    my_year='21'+str(my_year)
print(my_year)

#Делаем список для больницы
lst1=(1,11,21,151,161,221,271,371,421,471,491,521,571,601,651)
lst2=(10,19,150,160,220,270,370,420,470,490,520,570,600,650,700)
lst3=('Больница Курессааре','Наистеклиник Тартуского университета',
      'Восточно-Таллиннская центральная больница родильный дом Пелгулинна Таллинн',
      'Больница Кейла','Больница Рапла, больница Локса, больница Хийумаа (Кярдла)',
      'Восточно-Вируская центральная больница (Кохтла-Ярве, бывший Йыхви)',
      'больница Маарьямыйса (Тарту), больница Йыгева', 'Нарвская больница',
      'Красивая больница','Больница Хаапсалу','Больница Ярвамаа (платная)',
      'Больница Раквере, Убей больницу','больница Валга','больница Вильянди',
      'Южно-эстонская больница (Выру), Пылвская больница')
#print(len(lst1),len(lst2),len(lst3))
#Проверка есть не верно составлен список
if len(lst1)!=len(lst2) or len(lst2)!=len(lst3):
    print('Списки разные длинны')
    quit()
for i in range(len(lst1)):
    if int(my_bolnica)>lst1[i] and int(my_bolnica)<lst2[i]:
        my_bolnica_name=lst3[i]
#print(my_bolnica_name)
#Проверка контрольного значение

lst4=(1,2,3,4,5,6,7,8,9,1)
lst5=(3,4,5,6,7,8,9,1,2,3)

sum1=0
sum2=0

for i in range(10):
    sum1 =sum1 + lst4[i]*int(user_id[i])
    sum2=sum2+ lst5[i]*int(user_id[i])
 #   print(str(lst4[i]), " ", str(user_id[i]),sum1)
print(sum1)

#Если 10 то проверяем на 0.
#Проверка на ключ
print(int(user_id[-1]))
if sum1-(sum1//11)*11 == int(user_id[-1]):
        print('Все ок')

if sum1 - (sum1 // 11) * 11 == 10 and int(user_id[-1]) == 0:
          print('Все ок')
#проверка 2 ключ
else:
    if sum2 - (sum2 // 11) * 11 == int(user_id[-1]):
        print('Все ок ключ2')

    if sum2 - (sum2 // 11) * 11 == 10 and int(user_id[-1]) == 0:
        print('Все ок ключ2')
    print('Не прошло ключевание ни 1 ни 2, проверьте 11 знак')
    quit()
print('You are ',My_pol,'. You birh day is ',my_date,'.',my_month,'.',my_year,".You hospidal is ",
      my_bolnica_name,'. You code is correct',sep='')