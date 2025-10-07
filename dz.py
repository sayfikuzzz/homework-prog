#1
"""def encryption():
    s = ''
    x = str(input('Введите текст для шифрования: '))
    y = int(input('Введите число сдвига:'))
    for i in x:
        s += chr(ord(i) + y) # сдвигаем на y вправо
    return s
'''
Шифрует текст.

X - начальная строка
y - число сдвига
s - зашифрованная строка
по итогу выводится строка s
'''

def decryption():  # дешифровка
    h = ''
    a = str(input('Введите текст для расшифровывания: '))
    b = int(input('Введите число сдвига:'))
    for i in a:
        h += chr(ord(i) - b) # сдвигаем на b влево
    return h
'''
Расшифровывает текст.

a - начальная строка
b - число сдвига
h - расшифрованная строка
по итогу выводится строка h
'''
print(encryption())
print(decryption())"""

#2
"""def check_winners(scores, student_score):
    if student_score not in scores:
      return 'Вас нет в списке'
    elif student_score in sorted(scores)[-3:]:
        return 'вы в тройке победителей!'
    else:
        return 'вы не попали в тройку победителей'
'''
Функция ищет количество баллов Стаса в списке.
сортируем список в порядке возрастания
и ищем в последних трёх числах число Стаса
scores —список, который содержит количество баллов каждого участника олимпиады
student_score — количество баллов, которое заработал Стас.
'''
ball = int(input('Введите своё количество баллов:'))
print(check_winners([1, 2, 3, 40, 50, 25, 24, 23], ball))"""

#3
"""def print_pack_report(count):
    if count > 1 and count == int(count):
        if count % 5 == 0 and count % 3 == 0:
            return f'{count} - расфасовываем по 3 или по 5'
        elif count % 5 == 0 and count % 3 != 0:
            return f'{count} - расфасовываем по 5'
        elif count % 5 != 0 and count % 3 == 0:
            return f'{count} - расфасовываем по 3'
        else:
            return f'{count} - не заказываем'
    else:
      return 'Число должно быть целое и больше единицы'
'''
функция print_pack_report() на вход принимает
целое положительное число больше единицы
и выводит информацию о том,
как можно расфасовать определённое количество пирожных.
count - число пирожных.

'''
k = int(input('Введите кол-во пирожных:'))
print(print_pack_report(k))"""

#4
"""import random

nizhn = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя' 

verhn = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def proverka(password):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    if len(password) < 5:
        print('В пароле должно быть хотя бы 5 символов')
        return

    for i in '0123456789':
        if i in password:
            count1 += 1
            break
    if count1 == 0:
        print('В пароле должна быть хотя бы одна цифра')

    for j in '!@#$%^&*':
        if j in password:
            count2 += 1
            break
    if count2 == 0:
        print('В пароле должен быть хотя бы один спецсимвол')

    for h in nizhn:
        if h in password:
            count3 += 1
            break
    if count3 == 0:
        print('В пароле должен быть хотя бы один нижний индекс')

    for w in verhn:
        if w in password:
            count4 += 1
            break
    if count4 == 0:
        print('В пароле должен быть хотя бы один верхний индекс')

    if count1 != 0 and count2 != 0 and count3 != 0 and count4 != 0:
        print('Отлично!')
'''
Функция проверяет введённый пользователем пароль на наличие
всех необходимых знаков.
nizhn - нижний регистр
verhn - верхний регистр
password - введённый пользователем пароль
'''
k = str(input('Вам нужно сгенерировать пароль (да/нет):')).lower()
if k == 'да' or k == 'da':
    c1 = random.choices('0123456789', k=random.randint(2, 5))
    c2 = random.choices(nizhn, k=random.randint(2, 5))
    c3 = random.choices(verhn, k=random.randint(2, 5))
    c4 = random.choices('!@#$%^&*', k=random.randint(2, 5))
    pass1 = c1 + c2 + c3 + c4
    random.shuffle(pass1)
    pass2 = ''.join(pass1)
    print(f'Сгенерированный пароль: {pass2}')
elif k == 'нет' or k == 'net':
    pas = str(input('Введите пароль: '))
    proverka(pas) # проверяем пароль с помощью функции proverka
elif k != 'нет' and k != 'net' and k != 'da' and k != 'да':
    print('Введите да или нет') """


#5
"""def to_roman(num): # Конвертирует арабское число в римское
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    # Строка для результата
    result = ""
    # Проходим по всем значениям в списке
    for i in range(len(values)):
        # Пока текущее число больше или равно значению из списка
        while num >= values[i]:
            # Добавляем соответствующую римскую цифру к результату
            result += numerals[i]
            # Вычитаем значение из исходного числа
            num -= values[i]
    # Возвращаем готовую римскую цифру
    return result


def from_roman(roman): #Конвертирует римское число в арабское
    # Словарь соответствия римских цифр арабским числам
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Переменная для накопления результата
    result = 0
    # Переменная для хранения предыдущего значения
    prev_value = 0

    # Проходим по строке справа налево
    for char in reversed(roman.upper()):
        # Получаем числовое значение текущего символа
        value = roman_dict[char]
        # Если текущее значение меньше предыдущего, вычитаем его
        if value < prev_value:
            result -= value
        # Иначе прибавляем его
        else:
            result += value
        # Сохраняем текущее значение как предыдущее
        prev_value = value

    # Возвращаем итоговое число
    return result


# Тестирование функций
roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]

print("Римские → Арабские:")
# Проходим по всем тестовым римским числам
for test in roman_tests:
    # Выводим исходное римское число и результат конвертации
    print(f"{test} → {from_roman(test)}")

print("\nАрабские → Римские:")
# Проходим по всем тестовым арабским числам
for i in [4, 9, 42, 99, 2023]:
    # Выводим исходное арабское число и результат конвертации
    print(f"{i} → {to_roman(i)}") """