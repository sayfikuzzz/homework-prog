import datetime
from decimal import Decimal


DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    # Преобразуем строку даты в объект datetime.date, если она передана
    if expiration_date:
        expiration_date = datetime.datetime.strptime(
            expiration_date, '%Y-%m-%d').date()

    # Создаем словарь с информацией о продукте
    goods = {
        'amount': Decimal(str(amount)),
        'expiration_date': expiration_date
    }

    # Добавляем продукт в словарь items
    if title in items:
        items[title].append(goods)  # Если продукт уже есть - добавляем в существующий список
    else:
        items[title] = [goods]  # Если продукта нет - создаем новый список


def add_by_note(items, note):
    """Добавляет продукт по текстовой заметке формата 'Название количество дата'"""
    parts = note.split()

    if len(parts) >= 3:
        expiration_date = parts[-1]  # Последняя часть - дата
        amount = parts[-2]  # Предпоследняя часть - количество
        title = ' '.join(parts[:-2])  # Все остальное - название продукта
    else:
        expiration_date = None  # Если частей меньше 3 - даты нет
        amount = parts[-1]  # Последняя часть - количество
        title = ' '.join(parts[:-1])  # Все остальное - название

    add(items, title, amount, expiration_date)


def find(items, needle):
    """
    Находит продукты по запросу (без учета регистра)
    Возвращает список названий продуктов, содержащих needle
    """
    results = []
    needle_lower = needle.lower()  # Приводим запрос к нижнему регистру

    # Ищем совпадения в названиях продуктов
    for product_name in items.keys():
        if needle_lower in product_name.lower():
            results.append(product_name)

    return results


def amount(items, needle):
    """
    Возвращает общее количество найденного продукта
    Суммирует amount всех партий найденных продуктов
    """
    found_products = find(items, needle)  # Находим продукты по запросу
    total_amount = Decimal('0')  # Начальное значение суммы

    # Суммируем количество всех партий найденных продуктов
    for product_name in found_products:
        for product_batch in items[product_name]:
            total_amount += product_batch['amount']

    return total_amount


# Начальные данные холодильника
goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}  # Вода без expiration_date
    ],
}

# Тестирование функций
add(goods, 'Сыр Гауда', 8, '2024-01-20')
add(goods, 'Йогурт греческий', 2, '2023-12-10')
add_by_note(goods, 'Колбаса сырокопченая 1.5 2024-02-15')

# Проверка количества продуктов
print(amount(goods, 'сыр'))  
print(amount(goods, 'йогурт'))  

# Вывод всего содержимого холодильника
for product in goods:
    print(f'"{product}": {goods[product]}')

# Проверка поиска
print(find(goods, 'гауда'))  # Поиск по части названия
print(find(goods, 'копченая'))  # Поиск по характеристике
