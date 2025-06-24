thislist=["apple","banana","cherry","orange"]
# thislist[1]="backcurrent"
# print(thislist)
# thislist[1:3]=["apple","watermelon"]
# print(thislist)
# thislist.insert(2,"banana")
# thislist.append("kiwi")
# print(thislist)

# tropical=["mango","pineapple","cherry"]
# thislist.extend(tropical)
# print(thislist)

# thislist.remove("apple")
# print(thislist)

# thislist.pop(3)
# print(thislist)

thislist.sort()
print(thislist)
list=thislist.copy()
print(list)


# tropical.clear()
# print(tropical)
# del tropical
# #print(tropical)
# print("tropical list was deleted")

# for i in thislist:
#     print(i)

# for i in range(0,len(thislist)):
#     print(thislist[i])/
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1
newlist=[]
for i in thislist:
    if "a" in i:
        newlist.append(i)       
print(newlist)


list1=["a","b","c"]
list2=[1,2,3,4]
for i in list2:
    list1.append(i)
print(list1)

list1=["a","b","c"]
list2=[1,2,3,4]
list1.extend(list2)
print(list1)
