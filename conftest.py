import pytest
from selenium.webdriver.remote.webelement import WebElement

from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Firefox()
    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()

@pytest.fixture()
def go_to_my_pets():
    '''Авторизация'''
    email_field: WebElement = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_field.send_keys(valid_email)
    password_field = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    )
    password_field.send_keys(valid_password)
    login_button = WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_button.click()
    my_pets_link = WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Мои питомцы"))
    )
    my_pets_link.click()