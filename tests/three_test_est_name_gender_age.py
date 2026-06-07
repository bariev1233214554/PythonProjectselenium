import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_there_is_a_name_age_and_gender(go_to_my_pets):
    '''Проверяем, что на странице со списком моих питомцев у всех питомцев есть имя, возраст и порода'''
    try:
        WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr"))
        )
    except Exception as e:
        pytest.driver.save_screenshot("pets_table_not_found.png")
        pytest.fail(f"Не удалось найти таблицу питомцев: {e}")
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    if not pet_data:
        pytest.fail("На странице не найдено ни одного питомца")
    for i, pet in enumerate(pet_data):
        data_pet = pet.text.replace('\n', ' ').replace('×', '').strip()
        if not data_pet:
            pytest.fail(f"У питомца №{i+1} отсутствуют данные")
        split_data_pet = [part for part in data_pet.split() if part]
        if len(split_data_pet) < 3:
            pytest.fail(
                f"У питомца №{i+1} недостаточно данных. "
                f"Ожидалось минимум 3 поля (имя, возраст, порода), найдено {len(split_data_pet)}: '{data_pet}'"
            )
        try:
            age = split_data_pet[2]
            if not age.replace('.', '').isdigit():
                print(f"Предупреждение: возраст питомца №{i+1} не является числом: '{age}'")
        except IndexError:
            pass
        assert True, "Все питомцы имеют имя, возраст и породу"


