import os
import random

clear = lambda: os.system('cls')

print('Привет! Я загадал слово, твоя задача - угадать его по буквам.')
input('*Нажми Enter, чтобы продолжить*')
clear()
print('Поехали!')
words = ['инновация', 'барабан', 'бабуин', 'банан', 'сом', 'маракас', 'планшет', 'пайтон', 'библиотека', 'комната']
word = random.choice(words)
hp = 10
letters = []

while hp > 0:
    is_win = True

    for symb in word:
        if symb in letters:
            print(symb, end=' ')
        else:
            print('*', end=" ")
            is_win = False
    print()
    if is_win:
        print('МОЛОДЕЦ!!!')
        break
    letter = input('Введите букву: ')

    letters.append(letter)
    clear()

    if letter not in word:
        hp -= 1
    print(f'У вас осталось {hp} попыток')

if hp == 0:
    print('Ты проиграл! У тебя закончились жизни')
    print(f'Правильное слово {word}')
