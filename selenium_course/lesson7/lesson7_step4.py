from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
time.sleep(5)
browser.execute_script("window.scrollBy(0, 100);")
button.click()
assert True