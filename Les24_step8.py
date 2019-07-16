from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Открыть страницу http://suninjuly.github.io/explicit_wait2.html
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

#Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
button1 = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"10000 RUR")
    )
button2 = browser.find_element_by_id("book")
button2.click()

#Решить уже известную нам математическую задачу 
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
response = browser.find_element_by_id("answer")
response.send_keys(y)
button3 = browser.find_element_by_id("solve")
button3.click()



