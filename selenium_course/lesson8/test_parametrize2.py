import pytest
from selenium import webdriver
import time
import math

links = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
message = []

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_alien_message(browser, link):
    browser.get(f"https://stepik.org/lesson/{link}/step/1")
    answer = math.log(int(time.time()))
    ansfield = browser.find_element_by_css_selector(".textarea")
    ansfield.send_keys(str(answer))
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    result = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert result == "Correct!", f"result is {result}"
