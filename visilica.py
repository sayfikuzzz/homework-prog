import random


def simple_hangman():
    words = ['кот', 'дом', 'лес', 'сон', 'мир', 'нос', 'рот', 'год', 'час', 'брат']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    used_letters = []

    print("Игра 'Виселица'!")
    print(f"Слово: {' '.join(guessed)}")

    while attempts > 0 and '_' in guessed:
        print(f"\nПопыток: {attempts}")
        letter = input("Буква: ").lower()

        if letter in used_letters:
            print("Уже было!")
            continue

        used_letters.append(letter)

        if letter in word:
            for i, l in enumerate(word):
                if l == letter:
                    guessed[i] = letter
            print("Есть такая буква!")
        else:
            attempts -= 1
            print("Нет такой буквы!")

        print(f"Слово: {' '.join(guessed)}")

    if '_' not in guessed:
        print(f"Победа! Слово: {word}")
    else:
        print(f"Проигрыш! Слово: {word}")


# Запуск
simple_hangman()