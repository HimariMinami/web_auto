from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    field1 = browser.find_element_by_name('firstname')
    field1.send_keys("alalal")
    field2 = browser.find_element_by_name('lastname')
    field2.send_keys("yayayaya")
    field3 = browser.find_element_by_name('email')
    field3.send_keys("hi.oleg.test+2@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(current_dir, 'file.txt')
    file_btn = browser.find_element_by_id('file')
    file_btn.send_keys(file)
    submit = browser.find_element_by_css_selector('.btn')
    submit.click()


finally:

    time.sleep(10)
    browser.quit()