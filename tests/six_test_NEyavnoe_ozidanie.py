import pytest
from settings import valid_email, valid_password
from selenium.webdriver.common.by import By

def test_show_pet_friends():
   '''Проверка карточек питомцев. Неявное ожидание'''
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
   assert len(names) > 0, "На странице нет питомцев — список имён пуст"
   assert len(images) == len(names) == len(descriptions), \
      f"Несоответствие количества элементов: изображений={len(images)}, имён={len(names)}, описаний={len(descriptions)}"
   for i in range(len(names)):
      img = images[i]
      src = img.get_attribute('src')
      assert src != '', f"У питомца №{i + 1} отсутствует атрибут 'src' у изображения"
      assert img.is_displayed(), f"Изображение питомца №{i + 1} скрыто (не видно на странице)"
      name_elem = names[i]
      name_text = name_elem.text
      assert name_text != '', f"У питомца №{i + 1} отсутствует имя"
      assert name_elem.is_displayed(), f"Имя питомца №{i + 1} скрыто"
      desc_elem = descriptions[i]
      desc_text = desc_elem.text
      assert desc_text != '', f"У питомца №{i + 1} отсутствует описание"
      assert desc_elem.is_displayed(), f"Описание питомца №{i + 1} скрыто"
      assert ',' in desc_text, f"В описании питомца №{i + 1} нет запятой: '{desc_text}'"
      parts = [part.strip() for part in desc_text.split(',')]
      assert len(parts) >= 2, f"Описание питомца №{i + 1} не содержит минимум двух частей: '{desc_text}'"
      for j, part in enumerate(parts):
         assert part != '', f"Часть {j + 1} описания питомца №{i + 1} пустая: '{desc_text}'"
