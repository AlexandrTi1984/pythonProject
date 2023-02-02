from My_eesti_Kod_Funct import gender_pol
from My_eesti_Kod_Funct import my_date_birthday
from My_eesti_Kod_Funct import bolnica_name
from My_eesti_Kod_Funct import chek_key_1_2
from My_eesti_Kod_Funct import my_chek_id

#user_id='38405230460'
#user_id='48203240071'
#user_id='38803160272'
#user_id='50605220085'
#user_id='60910050039'
#user_id='62009010247'


user_id = input('Введи ид код для дальнейшей работы ')
#my_chek_id(user_id)
while True:
    user_choice = input("Выберите что хотите проверить:\n1.Пол \n2.Дата рождения \n"
                        "3.Регион \n4.Проверка кода \n5.Ввести код\n0.Выход\n--> ")

    if user_choice == '1':
        print('Ваш пол:', gender_pol(user_id[0]))
    elif user_choice == '2':
        print('Ваша дата рождения:', my_date_birthday(user_id[5:7],user_id[3:5],user_id[0],user_id[1:3]))
    elif user_choice == '3':
        print('Ваша больница:', bolnica_name(user_id[0],user_id[1:3],user_id[7:10]))
    elif user_choice == '4':
        print('Ваш код', chek_key_1_2(user_id[0:10],user_id[-1]))
    elif user_choice == '5':
        while True:
            user_id = input('ВВеди ид код или напиши exit для выхода или 0000 ')
            if str(user_id.lower()) == ('exit') or user_id.lower() == ('0000'):
                print('Спасибо что пользовались нашим сервисом')
                quit()
            try:
                int(user_id)  # проверка на число
                if len(user_id) != 11:
                    raise Exception
            except ValueError:
                print("Введено не число")
                continue
            except Exception:
                if len(user_id) > 11:
                    print('Код длинный')
                else:
                    print('Код короткий')
                continue
            else:
                print('Ваш код', user_id)
                break
    elif user_choice == '0':
        quit()
    else:
        print('Choice is out of range!')
    print('Введите новый запрос ниже:')
print('Good bye')