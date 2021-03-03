#Tell number is prime or not

def prime(x):
    if x>1 :
        for i in range(2,x):
            if(x%i==0):
                print("Not a prime number")
                break;
            else:
                print("Given number is Prime number")
                break;
    else:
        print("Not a prime number")

num = int(input("enter number"))
result = prime(num)

        
