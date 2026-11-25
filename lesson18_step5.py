import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN = "ТВОЙ_EMAIL_ОТ_STEPIK"
PASSWORD = "ТВОЙ_ПАРОЛЬ_ОТ_STEPIK"

LINKS = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Safari()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.parametrize("link", LINKS)
def test_alien_message(browser, link):
    wait = WebDriverWait(browser, 15)
    browser.get(link)

    # 1. Нажимаем кнопку "Войти" и авторизуемся
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login")))
    login_button.click()

    browser.find_element(By.NAME, "login").send_keys(LOGIN)
    browser.find_element(By.NAME, "password").send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ждём, пока модальное окно авторизации исчезнет
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog")))

    # 2. Ждём пустое поле ответа и вводим актуальное число
    textarea = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area")))
    textarea.clear()
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)

    # 3. Нажимаем кнопку "Отправить"
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    submit_btn.click()

    # 4. Дожидаемся появления опционального фидбека и проверяем текст
    hint = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    hint_text = hint.text

    assert hint_text == "Correct!", f"Expected 'Correct!', but got: '{hint_text}'"