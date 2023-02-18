import requests
from bs4 import BeautifulSoup as BS

my_url='https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
full_page=requests.get(my_url,headers=headers)

soup=BS(full_page.content,'html.parser')
rate=soup.find_all('tbody') #одно значение, findall все искать
print(soup.td.string)

# Getting all data using findAll
#match = soup.findAll("td", class_="number")
# match = soup.find_all("td")

# my_list=[]
# for p1 in rate:
#      plist1 = list(p1)
#      print(p1)
#      print(plist1)
#      my_list.append(plist1)
#
