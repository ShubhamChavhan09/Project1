import random

print('Hello. What is your name? ')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secretnumber = random.randint(1,20)

for guessestaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretnumber:
        print('Your guess is toolow.')
    elif guess > secretnumber:
        print('your guess is too high.')
    else:
        break #condition for correct guess!

if guess == secretnumber:
    print('Good job' + name + '!You gussed my numbre in ' + str(guessestaken) + 'guesses!')
else:
    print('Nope.The number I was thinking of was' + str(secretnumber))
