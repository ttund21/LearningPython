from random import randint

secretNumber = randint(1,20)
guess = None
chance = 6 

print('Welcome to Guess The Number Game!\n')
print('Rules:\n1 - U have 5 chances\n2 - Try to hit number between 1 and 20\n')

for i in range(5):
    chance = chance - 1
    print('\nNumber of chances:', chance)
    try:
        print('Guess the Number: ')
        guess = int(input('>>> '))
    except ValueError:
        print('Invalid Value')

    try:
        if guess > secretNumber:
            print('Too High')
        elif guess < secretNumber:
            print('Too Low')
        else:
            print('U Hit')
            break
    except TypeError:
        print()

if guess == secretNumber:
    print('\nU win!')
else:
    print('\nU lose')
