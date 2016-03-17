import random

answer = random.randint(0,5)
count = 3
print "LET'S GUESS A NUMBER"
print "Hint: This number is between 0-5"
print "And you have 3 times to guess"

while count >0:
    guess = input("Guess please!")
    count -=1
    if guess == answer:
        print "CORRECT"
        break
    else:
        print "WRONGGGGG!"
        print "You have %d time(s) left" %count
print "The answer is %d" %answer