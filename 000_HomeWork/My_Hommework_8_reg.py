import re
text_to_search = '''
1. Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.
	HASH цвета используют значения от 0 до 15, где 0-9 цифры от нуля до 9, 10-15 буквы от A-F.

2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +. (Примеры выражени

3. Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:30». Учтите, что «37:98» – некорректное время.

4. Написать программу котороая будет выбирать из файла people.txt:
	1) Все имена и фамилии
	2) Все адреса

5. Написать регулярное выражение для проверки строки, задача определить состоит ли строка из символов a-z, A-Z, 0-9.

6. Написать регулярное выражение для определения эстонского личного кода (isikukood)

Все строки произвольные.

Задание 1: цвета 
#90EE90
#FF69B4
#20B2AA

Задание 2:
Примеры выражений “2*3-1-5” или (4+5)-9*4
Примеры выражений “5*9+3*7” 

Задание 3:
Часы и время:
завтрак 9:12  9:88  33:15
обед 12:39    14:78 27:15
ужин 20:47    00:05 


Задание 6
#user_id='38414230460' False
#user_id='48203240071' True
#user_id='38833160272' False
#user_id='50605320085' False
#user_id='60910050039' True
#user_id='62029010247' False

'''
str_formula='2*9+3*5'

#  Number1 #
#pattern = re.compile(r'(#)[0-F]{6}')
pattern = re.compile(r'#[0-9A-F]{6}',re.IGNORECASE)
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


#  Number2 #
pattern = re.compile(r'[+]\d+')
matches = pattern.finditer(str_formula)
for match in matches:
    print(match)


#  Number3 #
pattern = re.compile(r'\b(([0-1][0-9])|(2[0-3])):[0-5][0-9]\b')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#  Number4 #
with open('people.txt', 'r', encoding='UTF8') as file:
    people_data = file.read()
    # Match
#pattern=re.compile(r'[A-Z][a-z]+\s+[A-Z][a-z]+\s')
pattern=re.compile(r'[A-Z][a-z ]+\s+[A-Za-z-]+\n')
names = pattern.findall(people_data)
count=0
# for match in names:
#     count+=1
#     print(match)

#pattern2=re.compile(r'\d{3}\s[\w]+\s[A-Z][a-z]., [A-Z][\w\s]+[A-Z]{2}\d{5}')
pattern2=re.compile(r'(\d{3} ).+\w+')
adress = pattern2.findall(people_data)

# count2=0
# for match2 in adress:
#     count2+=1
#     print(match2)
#
# print('Всего ФИО ',count)
# print('Всего адресов ',count2)

people_pairs=list(zip(names,adress))
people_dict={}
cnt=0
for x,y in people_pairs:
    people_dict[cnt]= {'ФИО':x, 'Адрес':y}
    cnt+=1
print(people_dict)
##### Number 5#####
my_str_example1='Aggg**99998888wwwqqqzzz'
my_str_example2='Aggg99998888wwwqqqzzz'
my_str_example3='Agg@g99998888wwwqqqzzz'

pattern = re.compile(r'\W')
pattern = re.compile(r'\W')
matches = pattern.finditer(my_str_example3)

count=0
for match in matches:
    count+=1

if count >0:
    print("Строка содержит не только A-z и 0-9")
else:
    print("Строка содержит только A-z и 0-9")

#Number 6 ##
pattern = re.compile(r'[1-8]\d{2}(([0]\d)|([1][0-2]))(([0-2][\d])|([3][01]))[0-8]\d{3}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)