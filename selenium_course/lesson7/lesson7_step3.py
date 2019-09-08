from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    answer = int(x) + int(y)
    dropdown1 = Select(browser.find_element_by_id('dropdown'))
    dropdown1.select_by_value(str(answer))
    submit = browser.find_element_by_css_selector('.btn')
    submit.click()


finally:

    time.sleep(10)
    browser.quit()