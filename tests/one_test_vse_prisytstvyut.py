import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_are_present(go_to_my_pets):
    '''Проверяем, что на странице со списком моих питомцев присутствуют все питомцы'''
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
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr"))
    )
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    number_of_pets = len(pets)
    assert number == number_of_pets
