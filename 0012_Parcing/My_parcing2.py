import requests
from bs4 import BeautifulSoup as BS
import re

url='https://gammatest.net/course/python/'

full_page=requests.get(url,timeout=3)
#print(full_page.text)

soup=BS(full_page.content,'html.parser')
#print(soup)
# print(soup.title)
# print(soup.table)
# print(soup.tr)
# print(soup.prettify()) #читаемый код
# print(soup.title.name)
# print(soup.title.text)
# print(soup.get_text)
# print(soup.div['class'])
# print(soup.a['href'])
#print(soup.title.parent)
#find находит только один елемент
# match = soup.find('div',class_='navbar-header')
# match1 = soup.find('div')
# match2 = soup.find(class_='navbar-header')
# match = soup.find_all('div',class_='col-md-4 col-sm-12') #матч єто список где все дивы
# print(len(match))
# #print(match[2])
# for div in match:
#    links = div.find_all('a') # а это а href єто супы из которого по атрибуты выкачиваем данные текст или сылка или id
#    for link in links:
#        print(link['href']) #это атрибут в скобках

#print(soup.contents[3]) # обращение по индексу в сайте до 4




# print(match1)
# print(match2)
# print(match.a['href'])

# print(soup.find(re.compile((r'^me'))))
# print(soup.find(string=re.compile((r'^Пе')))) #обращение к элементы и ищем так текст
# print(soup.find(string=re.compile((r'^Пе'))))
# print(soup.find_all(['a','table']))

# for tag in soup.find_all(True): #Находит все теги
#     print(tag)
#
# print(soup.find_all(string=True))#все теги где есть текст
# print(soup.find_all('a',string='Перейти',limit=2)) #количество 2

test_link=soup.find('a',string='Eesti keeles')
# print(test_link.find_parents())# всех
# print(test_link.find_parents('div'))
#
# print(test_link.find_parent()) # ближайщего родителя
# print(test_link.find_next_siblings())
print(test_link.find_previous_siblings()) #следующий родитель
#print(soup.find_all_next())
print(soup.find('div',class_='col-md-4').find_next_siblings())