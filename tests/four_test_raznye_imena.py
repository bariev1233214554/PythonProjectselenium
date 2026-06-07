import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_have_different_names(go_to_my_pets):
    '''Проверяем, что на странице со списком моих питомцев у всех питомцев разные имена'''
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr"))
    )
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    if not pet_data:
        pytest.fail("На странице не найдено ни одного питомца")
    pets_name = []
    for i, pet in enumerate(pet_data):
        data_pet = pet.text.replace('\n', ' ').replace('×', '').strip()
        split_data_pet = data_pet.split()
        if split_data_pet:
            name = split_data_pet[0]
            if name:
                pets_name.append(name)
            else:
                pytest.fail(f"У питомца №{i+1} отсутствует имя в данных: '{data_pet}'")
        else:
            pytest.fail(f"Не удалось извлечь данные у питомца №{i+1}: '{data_pet}'")
    unique_names = set(pets_name)
    duplicates_count = len(pets_name) - len(unique_names)
    from collections import Counter
    name_counts = Counter(pets_name)
    duplicate_names = [name for name, count in name_counts.items() if count > 1]
    assert duplicates_count == 0, (
        f"Найдены повторяющиеся имена питомцев: {duplicate_names}. "
        f"Всего дубликатов: {duplicates_count}"
    )

