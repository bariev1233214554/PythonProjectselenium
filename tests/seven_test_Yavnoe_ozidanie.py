import pytest
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_show_my_pets():
   '''Проверяем что мы оказались на странице "Мои питомцы". Явное ожидание'''
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   login_button = WebDriverWait(pytest.driver, 10).until(
       EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
   )
   login_button.click()
   my_pets_link = WebDriverWait(pytest.driver, 10).until(
       EC.element_to_be_clickable((By.LINK_TEXT, "Мои питомцы"))
   )
   my_pets_link.click()
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

