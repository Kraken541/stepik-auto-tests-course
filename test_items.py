import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    # Раскомментируй строку ниже, если хочешь сам проверить визуально с --language=fr
    # time.sleep(30)
    add_to_basket_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_basket_buttons) > 0, "Add to basket button is not found on the page"