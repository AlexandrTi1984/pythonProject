import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
#
# driver.get('https://github.com/')
#
# # driver.close() #закрывает текщую вкладку
# # driver.quit() #закрывает хром
# #print(driver.title)
# email=driver.find_element('id','user_email')
# # if email.is_displayed(): # не скрытое
# #     if email.is_selected():
# #if email.is_enabled(): # доступно ли
# email.send_keys('anbe22u@mail.ru') #передача в поле емаил
# email.send_keys(Keys.ENTER)
# #
# # try:
# #     element=WebDriverWait(driver,20).until(
# #         EC.element_to_be_clickable((By.XPATH,'//*[@id="username-container"]/div[2]/button'))
# #     )
# #     element.click()
# # except:
# #     print('Error')
# #     driver.quit()
# # # cont=driver.find_element('xpath', '//*[@id="username-container"]/div[2]/button')
# # # time.sleep(15)
# # # cont.click()
#
# #time.sleep(5)
# # print(email)
# #https://selenium-python.readthedocs.io/waits.html
# def wait_till_clickable(driver, selector_type, selector_value, time):
#     try:
#         element = WebDriverWait(driver, time).until(
#             EC.element_to_be_clickable((selector_type, selector_value))
#         )
#     except:
#         print('error')
#         return None
#     else:
#         return element
#
# cont = wait_till_clickable(driver, By.XPATH, '//*[@id="email-container"]/div[2]/button', 15)
# if cont:
#     cont.click()
#
# time.sleep(5)

# driver = webdriver.Chrome()
# # driver.get('https://gammatest.net/')
# #
# link = driver.find_element('partial link text','Rohkem')
# link.click()
# time.sleep(5)
#
# driver.back() #Кнопка назад где вкладка
# time.sleep(2)
# driver.forward()#Кнопка вперед где вкладка
# driver.refresh()#Кнопка обновить где вкладка
#
# link = driver.find_elements('tag name','a')
#     for i in link:
#         print(i.get_attribute())

# driver = webdriver.Chrome()
#
# url='https://www.youtube.com/@visitestoniaofficial/videos'
# width=driver.get_window_size().get('width')
# heigth=driver.get_window_size().get('height')
# print(width,heigth)
# driver.set_window_size(800,600)
# driver.get(url)
# position=driver.get_window_position()  #координаті окна
# print(position)
# #time.sleep(5)
# driver.set_window_position(100,100)
# driver.set_window_rect(100,100,100,100) #параметры квадрата окна
# driver.fullscreen_window() #полній єкран
# time.sleep(5)
# driver.minimize_window() #свернуть, при этом драйвер будет работать
# time.sleep(5)
# driver.maximize_window()  #максимальный
# time.sleep(5)
driver = webdriver.Chrome()

url='https://www.youtube.com/@visitestoniaofficial/videos'

driver.get(url)
time.sleep(65)
#кнопка клик и нажатие
#accept=<span jsname="V67aGc" class="VfPpkd-vQzf8d" aria-hidden="true">Принять все</span>
#accept.click()
#driver.save_screenshot('Pic.png')
#
# element=driver.find_element('xpath','путь')

