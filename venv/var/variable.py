# Это игра по угадыванию чисел

import random

guessesTaken = 0

print('Привет! Как тебя зовут?')

myName = input()

number = random.randint(1,20)
print(myName + ', в какую игру ты хочешь поиграть?' ) #, я загадываю число от 1 до 20. А ты попробуй угадать. У тебя есть 6 попыток')
print('Напиши цыфру:')
print('1 - Угадай цифру')
print('2 - Царство драконов')
answer = input()

if answer == '1':
    for guessesTaken in range(6):
        print('Попробуй угадать.')
        guess = input()
        guess = int(guess)

        if guess < number:
            print('Твое число меньше')

        if guess > number:
            print('Твое число больше')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

    if guess != number:
        number = str(number)
        print('Увы. Я загадала число' + number + '.')
elif answer == '2':
    print('''Вы находитесь в землях, заселенных драконами. 
    Перед собой видете две пещеры. В одной из них - дружельбный дракон,
    который готов поделится с воми своими сокровищами. Во второй - 
    жадный и голодный дракон, который мигом вас съест.''')
    print()

    def chooseCave():
        cave = ''
        while cave != '1' and cave != '2':
            print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
            cave = input()
        return cave

    def checkCave(chosenCave):
        print('Вы приближаетесь к пещере...')
        time.sleep(2)
        print('Ее темнота заставляет вас дрожать от страха...')
        time.sleep(2)
        print('Большой дракон выпрыгивает перед вами! Он раскрывает свою ограмную пасть и ....')
        print()
        time.sleep(2)

        friendlyCave = random.randint(1,2)

        if chosenCave == str(friendlyCave):
            print('... делится с вами своими сокровищами!')
        else:
            print('... моментально вас съедает!')
else:
    print('Кажется, в условии нет такой цифры. Попробуй еще раз')

