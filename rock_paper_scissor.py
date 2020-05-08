import random
print('''Winning rules for Rock paper and scissor game are:
    Rock vs paper > paper wins
    Rock vs scissor > Rock wins
    paper vs scissor > scissor wins\n''')

while True:
    print('''Enter choice
             1. Rock
                2. paper
                    3. scissor''')
    choice = int(input('User turn: '))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid input: '))


    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print('\nUser choice is: ' + choice_name)
    print("\nNow it's computer's turn.....\n")

    comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'

    elif comp_choice ==2:
        comp_choice_name = 'paper'

    else:
        comp_choice_name = 'scissor'

    print('Computer choice is: ' + comp_choice_name)
    print('\n'+choice_name + ' v/s ' + comp_choice_name)

    #condition for winning
    if ((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
        print('paper wins =>', end='')
        result = 'paper'

    elif ((choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2)):
        print('scissor wins => ', end = '')
        result = 'scissor'

    else:
        print('Rock wins =>', end = '')
        result = 'Rock'
    #winner
    if result  == choice:
         print(' --- <== User wins ==>')
    else:
         print(' --- <== Computer wins ==>')
    print('Do you want to play again? (Y/N)')
    ans = input()
    if ans.upper() == 'N':
        break
print('\nThanks for playing')

         


    

                                     
    
    
    
