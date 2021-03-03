#Take two list and write a program that returns a list that containd only the elements that are common between the list(without duplicates)

firstList = [1,4,2,1,5,6,2,7,8,3,9,4,6]
secondList = [5,7,11,3,7,22,75,4,2,1,3,3,6,7]
newList = []
resultantList = []
for m in firstList:
    for n in secondList:
        if m==n:
            newList.append(m)
for x in newList:
    if x not in resultantList:
        resultantList.append(x)
print(resultantList)
            
