from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_id('robotCheckbox')
    checkbox1.click()
    radio1 = browser.find_element_by_id('robotsRule')
    radio1.click()
    submit = browser.find_element_by_css_selector('.btn')
    submit.click()


finally:

    time.sleep(10)
    browser.quit()