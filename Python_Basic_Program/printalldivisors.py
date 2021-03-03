#Find divisiables of given number in specific range

x = range(2,10)
y = int(input("enter the num : "))
newlist = []
for i in x:
    if i%y == 0:
        newlist.append(i)

print("All divisiable of ",y ,"are" , newlist)
