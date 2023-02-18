from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_till_clickable(driver, selector_type, selector_value, time):
    try:
        element = WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((selector_type, selector_value))
        )
    except:
        print('error')
        return None
    else:
        return element

driver = webdriver.Chrome()
url = 'https://www.saucedemo.com/'
driver.get(url)
driver.maximize_window()
my_login = driver.find_element('id','user-name')
my_login.send_keys('standard_user')
time.sleep(1)
my_pass = driver.find_element('id','password')
my_pass.send_keys('secret_sauce')
time.sleep(1)
my_button = driver.find_element('id','login-button')
my_button.send_keys(Keys.ENTER)

#Включили сотрировку
my_sort = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[2]/span/select')
my_sort.click()
my_sort.send_keys(Keys.DOWN)
time.sleep(1)
my_sort.send_keys(Keys.DOWN)
my_sort.send_keys(Keys.ENTER)
time.sleep(1)
#Добавляем в корзину
my_button_order1 = driver.find_element('id','add-to-cart-sauce-labs-bike-light').click()
time.sleep(1)
my_button_order2 = driver.find_element('id','add-to-cart-sauce-labs-bolt-t-shirt').click()
time.sleep(1)
my_button_order4 = driver.find_element('id','add-to-cart-sauce-labs-onesie').click()
time.sleep(1)
my_button_order3 = driver.find_element('id','add-to-cart-sauce-labs-backpack').click()
time.sleep(1)

#Удаляем в главном меню
my_button_order2re = driver.find_element('id','remove-sauce-labs-backpack').click()

time.sleep(1)
#Нажимаем корзину
my_basket = driver.find_element('id','shopping_cart_container').click()
time.sleep(2)
#Удаляем из корзины при оформлении
my_basket_remove_button = driver.find_element('id','remove-sauce-labs-onesie')
my_basket_remove_button.click()
time.sleep(2)
my_button_chekout = driver.find_element('id','checkout')
my_button_chekout.click()
my_pole_name = driver.find_element('id','first-name')
my_pole_name.send_keys('Alexandr')
my_pole_lastname = driver.find_element('id','last-name')
my_pole_lastname.send_keys('Tischenkov')
my_pole_adres = driver.find_element('id','postal-code')
my_pole_adres.send_keys('80017, Pärnu')
time.sleep(2)
my_button_cont = driver.find_element('id','continue').click()
time.sleep(1)
driver.save_screenshot('my_picture.png')
time.sleep(2)
my_button_finish = driver.find_element('id','finish').click()
time.sleep(2)
my_button_logout = driver.find_element('id','react-burger-menu-btn').click()

#Выход когда будет возможность делаем через функцию
time.sleep(1)
my_logout = wait_till_clickable(driver, By.ID, 'logout_sidebar_link', 10)
if my_logout:
    my_logout.click()

time.sleep(2)
driver.quit()
