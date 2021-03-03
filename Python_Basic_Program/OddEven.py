#Find the number which is odd/even and if divisible by 4

num = int(input("Enter any number : "))
check = int(input("Enter number to check is divided by : "))

if (num%2 == 0):
        print("Number is even")
if (num%4 == 0):
        print("Number is divisiable by 4")
if (num%2 !=0):
    print("number is odd")

if (num%check==0):
    print("number is dividiable by check",check)
