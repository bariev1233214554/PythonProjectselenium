import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_photo_availability(go_to_my_pets):
    '''Проверяем, что на странице со списком моих питомцев хотя бы у половины питомцев есть фото'''
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]"))
    )
    statistic = pytest.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]")
    stat_text = statistic[0].text
    number_str = stat_text.split('\n')[1].strip()
    if ':' in number_str:
        number = int(number_str.split(':')[1].strip())
    else:
        number = int(''.join(filter(str.isdigit, number_str)))
    half = number // 2
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')
    number_of_photos = 0
    for img in images:
        src = img.get_attribute('src')
        if src and src.strip():
            number_of_photos += 1
    assert number_of_photos >= half
    print(f'количество фото: {number_of_photos}')
    print(f'Половина от числа питомцев: {half}')