from My_eesti_Kod_Funct import gender_pol
from My_eesti_Kod_Funct import my_date_birthday
from My_eesti_Kod_Funct import bolnica_name
from My_eesti_Kod_Funct import chek_key_1_2

user_id='48203240070'
while True:
    user_choice = input("Выберите что хотите проверить:\n1.Пол \n2.Дата рождения \n"
                        "3.Регион \n4.Проверка кода \n5.Ввести код\n0.Выход\n--> ")

    if user_choice == '1':
        print('Ваш пол:', gender_pol(user_id[0]))
    elif user_choice == '2':
        print('Ваша дата рождения:', my_date_birthday(user_id[5:7],user_id[3:5],user_id[0],user_id[1:3]))
    elif user_choice == '3':
        print('Ваша дата рождения:', bolnica_name(user_id[7:10]))
    elif user_choice == '4':
        print('Ваш код', chek_key_1_2(user_id[-1]))
    elif user_choice == '5':
        break
    elif user_choice == '0':
        quit()
    else:
        print('Choice is out of range!')
    print('Введите новый запрос ниже:')
print('Good bye')