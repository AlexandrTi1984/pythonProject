import requests
#import antigravity
from requests.exceptions import HTTPError

#200 - успешное соединение
#300 - переадресация
#400 - ошибка клиента, 404 - клиент запрашивает не сушествующий файл
#500 - ошибка сервера, заблочен вход
#'https://xkcd.com/353/'

#Либо сылка либо api который джайсон возвращает
# r = requests.get('https://xkcd.com/353/',timeout=3)
# #получение инфо с сайта
# print(r.text)
# print(r.content)
#
# # pic =requests.get('https://xkcd.com/353/',timeout=3)
# # #'wb'  бинарній файл
# # with open('com1.png','wb') as file:
# #     file.write(pic.content)
# print(r.status_code)
# print(r.ok)
# print(r.headers)
# print(r.encoding)
# print(r.cookies)

for url in ['https://api.github.com','https://api.github.com/invalid']:
    try:
        response=requests.get(url)
        response.raise_for_status()
        x = 1/0
    except HTTPError as http_err:
        print(f'Ошибка {http_err}')
    except Exception as err:
        print(f'Ошибка {err}')
    else:
        print('Все хорошо')

