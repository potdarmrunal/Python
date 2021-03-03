#Number guessing game in python

import random
import math

lowerValue = int(input("Enter Lower Bound Value :"))
upperValue = int(input("Enter Upper Bound Value :"))
count = 0
x = random.randint(lowerValue,upperValue)

while(count < math.log(upperValue-lowerValue+1,2)):
    count = count + 1
    guess = int(input("Enter the value which you are guessing"))

    if x == guess:
        print("Congrats You Win!! :)")
        break
    elif x < guess:
        print("Sorry you guessed too small :( ")
    else:
        print("Sorry you guessed too large :( ")

if count >= math.log(upperValue - lowerValue+1,2):
    print("Sorry you used all your chances , Better Luck Next Time!!");
    

#math.log -> Is a mathemathical logarithumic function which returns the natural logarithum of a number or log of number to base
