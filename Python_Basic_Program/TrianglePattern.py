#print Following Pattern
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5 

def PrintTriangle1(x):
    num = 1
    for i in range(0,x):
        num = 1
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print("\r")

PrintTriangle1(5)


#print Following Pattern
#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15

def PrintTriangle2(x):
    num = 1
    for i in range(0,x):
        for j in range(0,i+1):
            print(num,end=" ")
            num = num + 1
        print("\r")

PrintTriangle2(5)

#print Following Pattern
#A
#A B
#A B C
#A B C D
#A B C D E

def PrintTriangle3(x):
    num = 65;
    for i in range(0,x):
        num = 65
        for j in range(0,i+1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1
        print("\r")
PrintTriangle3(5)

