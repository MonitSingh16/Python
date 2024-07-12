import random
import math

#taking inputs

lower = int(input("Enter Lower Bound:- "))
upper = int(input("Enter Upper Bound:- "))

x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1,2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")
#count and flag are two variables
count = 0
flag = False

while count < total_chances:
    count = count + 1

    guess = int(input("Guess a number:- "))

    if guess == x:
        print("Congratulations you did it in ", count, " try")
        flag = True
        break
    elif x > guess:
        print("You guessed it too small!")
    elif x < guess:
        print("You guessed it too high!")

if not flag:
    print("\n The number is %d" % x)
    print("\t Better uck Next Time!")





