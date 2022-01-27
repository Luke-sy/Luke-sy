# This is a guess the number game
import random
print('Hello. What`s your name?')
playerName = input()
if len(playerName) == 0:
    print('\'Oh look at me, I didn\'t write my name\'. I will call you \"Bob\"')
    playerName = 'Bob'
print('Well, ' + playerName + ', I am thinking of a number between 1 and 20')
print('You have 6 tries')
secretNumber = random.randint(1,20)


for guessesTaken in range(1,7):
    print('Go, take a guess.')
    try:
        guess = int(input())
        if guess < secretNumber:
            print('Your number is too low. Try again')
        elif guess > secretNumber:
            print('Your number is too high. Try again')
        else:
            break
    except ValueError:
        print('You did not enter a number')
try:
    if guess == secretNumber:
        print('Well done, ' + playerName + '. You guessed my number in ' + str(guessesTaken) + ' guesses.')
    else:
        print('Nope, you failed the 6 tries, ' + playerName + '. My number was ' + str(secretNumber))
except NameError:
    print('You did not even try')