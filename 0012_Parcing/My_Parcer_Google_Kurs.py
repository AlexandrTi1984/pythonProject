import requests
from bs4 import BeautifulSoup as BS

my_url='https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=rehc&aqs=chrome.1.69i57j0i10i131i433i512j0i131i433j0i10i131i433i512l3j0i10i512j0i10i131i433i512j0i10i512j0i131i433.2989j0j7&sourceid=chrome&ie=UTF-8'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
full_page=requests.get(my_url,headers=headers)
soup=BS(full_page.content,'html.parser')
# print(full_page)
# print(full_page.headers)

rate=soup.find('span', class_='DFlfde SwHCTb') #одно значение, findall все искать

rate=float(rate['data-value'])
print(rate)
user_sum=float(input('Введите сумму : '))
print(rate*user_sum)