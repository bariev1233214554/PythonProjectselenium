import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from collections import Counter

def test_no_duplicate_pets(go_to_my_pets):
    '''Проверяем, что на странице со списком моих питомцев нет повторяющихся питомцев'''
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr"))
    )
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    if not pet_data:
        pytest.fail("На странице не найдено ни одного питомца")
    pets_info = []
    for i, pet in enumerate(pet_data):
        data_pet = pet.text.replace('\n', ' ').replace('×', '').strip()
        if not data_pet:
            pytest.fail(f"У питомца №{i+1} отсутствуют данные")
        pets_info.append(data_pet)
    pet_counts = Counter(pets_info)
    duplicates = {pet: count for pet, count in pet_counts.items() if count > 1}
    if duplicates:
        duplicate_messages = []
        for pet_data, count in duplicates.items():
            duplicate_messages.append(f"'{pet_data}' (встречается {count} раз)")
        pytest.fail(
            f"Найдены повторяющиеся карточки питомцев:\n" +
            "\n".join(duplicate_messages)
        )
    assert not duplicates, "Обнаружены дублирующиеся карточки питомцев"
