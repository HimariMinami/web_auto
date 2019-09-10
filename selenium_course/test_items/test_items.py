import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_chart_button_found(browser):
    browser.get(link)
    time.sleep(10)
    add_to_chart_btn = browser.find_elements_by_css_selector("#add_to_basket_form > button")
    assert len(add_to_chart_btn) > 0, "There is no 'Add to chart' button"
