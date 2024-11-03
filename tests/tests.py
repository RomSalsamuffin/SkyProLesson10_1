from src.masks import get_masks_account, get_masks_card_number


def test_function(number, function, data):
    """Функция для проверки реализованных функций, принимающих один аргумент.
    number - номер теста
    function - имя тестируемой функции
    data - данные, принимаемые тестируемой функцией"""
    try:
        result = function(data)
    except Exception as e:
        result = f"Произошла ошибка: {e.__class__} {e.__str__()}"
    print(f"""тест №{number}. Input: {type(data)} {data}. Output: {result}""")


# Тесты

print("Функция get_masks_card_number:")

# тест №1. Задаем функции get_masks_card_number номер карты в верном формате (тип int, 16 цифр)
test_function(1, get_masks_card_number, 7000792289606361)

# тест №2. Задаем функции get_masks_card_number номер карты в верном формате (тип str, символы-только цифры,
# 16 символов)
test_function(2, get_masks_card_number, "7000792289606361")

# Задаем функции get_masks_card_number номер карты в неверном формате (тип int, меньше 16 символов)
test_function(3, get_masks_card_number, "70007926361")

# Задаем функции get_masks_card_number номер карты в неверном формате (тип str, в номере есть буквенные символы)
test_function(4, get_masks_card_number, "A000792289606361")

# Задаем функции get_masks_card_number номер карты с неверным типом данных (тип list)
test_function(5, get_masks_card_number, [1, 2, 3])

print("Функция get_masks_account:")
# Задаем функции get_masks_card_account номер счета в верном формате (тип int)
test_function(1, get_masks_account, 73654108430135874305)

# Задаем функции get_masks_card_account номер счета в верном формате (тип str, символы-только цифры)
test_function(2, get_masks_account, "73654108430135874305")

# Задаем функции get_masks_card_account номер счета в неверном формате (тип str, в номере есть буквенные символы)
test_function(3, get_masks_account, "A3654108430135874305")

# Задаем функции get_masks_card_account номер счета с неверным типом данных (тип list)
test_function(4, get_masks_account, [1, 2, 3])
