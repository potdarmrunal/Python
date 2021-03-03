#Find even numbers in a list

a = [1,4,9,16,25,36,49,64,81,100]
resultantList = []
for i in a:
    if(i%2==0):
        resultantList.append(i)
print("Even numbered list", resultantList)
