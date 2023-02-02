import csv
from My_functions import my_menu
from My_functions import my_menu2
from My_functions import my_top
while True:
    user_choice = input("Выберите Какой показатель проверить\n1.Social support \n2.Healthy life expectancy \n"
                        "3.Freedom to make life choices \n4.Generosity \n5.Perceptions of corruption\n"
                        "\n0.Выход\n--> ")
    user_choice2 = input("Выберите ТОП или введите свой топ цифру до 155\n1.Топ-3 \n2.Топ-5 \n3.Топ-10 \n\n0.Выход\n--> ")
    my_top(my_menu(user_choice),my_menu2(user_choice2)) # вызываем функцию топа
    print('Введите новый запрос ниже:')
print('Good bye')
