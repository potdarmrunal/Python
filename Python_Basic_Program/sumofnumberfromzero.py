#Accept number from user and calculate the sum of all number from 1 to a given number

def sumofnumber(x):
    sum = 0
    for i in range(1,x+1,1):
        sum = sum + i
    print("Total Sum",sum)

sumofnumber(10)
