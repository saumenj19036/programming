"""" A simple Rock, Paper, Scissors game.
First to get 3 points wins. """
import random
my_score = 0
computer_score = 0
computer_list = ['Rocks', 'Paper', 'Scissors']

while True:
    i_got = input('Give "r" for a Rock, "p" for a paper or "s" for a scissors: ')
    computer_got = random.choice(computer_list)

    if i_got == 'r' and computer_got == 'Paper':
        print('\nYou chose a Rock and computer chose a Paper, Computer got 1 point:\n')
        computer_score += 1
        print('You have() points and computer has () point'.format(my_score, computer_score))
    elif i_got == 'r' and computer_got == 'Scissors':
        print('\nYou chose a Rock and computer chose a Scissors, You got 1 point:\n')
        my_score += 1
        print('You have() points and computer has () point'.format(my_score, computer_score))
    elif i_got == 'p' and computer_got == 'Rock':
        print('\nYou chose a paper and computer chose a Rock, You got 1 point:\n')
        my_score += 1
        print('You have() points and computer has () point'.format(my_score, computer_score))
    elif i_got == 'p' and computer_got == 'Scissors':
        print('\nYou chose a paper and computer chose a Scissors, Computer got 1 point:\n')
        computer_score += 1
        print('You have() points and computer has () point'.format(my_score, computer_score))    
    elif i_got == 's' and computer_got == 'rock':
        print('\nYou chose a scissors and computer chose a rock, Computer got 1 point:\n')
        computer_score += 1
        print('You have() points and computer has () point'.format(my_score, computer_score))    
    elif i_got == 's' and computer_got == 'paper':
        print('\nYou chose a scissors and computer chose a paper, You got 1 point:\n')
        my_score += 1
        print('You have() points and computer has () point'.format(my_score, computer_score))              
    else:
        print('\nYou both chose the same.\n')

        """ Checking for score"""                  
    if my_score == 3:
        print('You won!')
        break 
    elif computer_score == 3:
        print('Computer won, better luck next time..')
        break
print('Game Over!')       