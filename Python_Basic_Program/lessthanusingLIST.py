#Write a program to create a new list which contains elements less than 5 in original list

listSize = int(input("Enter list size: "))
listdata = []
newList = []
for x in range(0,listSize):
    l = int(input())
    listdata.append(l);
for x in listdata:
    if x < 5:
        newList.append(x)

print("Newlist: ", newList)
print("Original List: ", listdata)
        
        
