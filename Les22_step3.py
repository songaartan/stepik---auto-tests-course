from selenium import webdriver

#Открыть страницу http://suninjuly.github.io/selects1.html
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

#Посчитать сумму заданных чисел
x_element = browser.find_element_by_id("num1")
y_element = browser.find_element_by_id("num2")
x = int(x_element.text)
y = int(y_element.text)
sum = x + y
sum2=str(sum)
print(x ,"+" , y, "=", sum)

#Выбрать в выпадающем списке значение равное расчитанной сумме

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(sum2)
#select.select_by_value("1") # ищем элемент с текстом "Python"
#Нажать кнопку "Отправить"

button = browser.find_element_by_css_selector("button.btn")
button.click()