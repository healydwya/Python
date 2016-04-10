import random
rando = random.randint(1,10)

print "You have entered a field where a bomb may go off. You have 3 tries to guess a number in order to disarm this bomb"

x = input("You have 3 guesses left. Enter a number to attempt to disarm the bomb: ")
control = rando

for num in range(1,3):
    if (x != control):
        print "Attempt: " + str(num) 
        guess2 = raw_input("Enter another number to try again: ")
    
    else:
        print "You solved it! Congratulations! Type python bomb.py to play again!"
        break
    
print "YOU DIED!!!!"
    