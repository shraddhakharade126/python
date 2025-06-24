# f=open("demo.txt")
# print(f.read())

# f=open("demo.txt")
# print(f.read(5))


# with open("demo.txt") as f:
#     print(f.read())  

# f=open("demo.txt")
# x=f.read()
# cnt=0
# for i in x:
#     if i==" ":
#         cnt+=1
# print("Space count  :",cnt)

def file():
    f=open("demo.txt","a")
    f.write("\nHello, I am a master in python programming.")
    f.close()
    f=open("demo.txt")
    print(f.read())
file()


# f=open("demo.txt","w")
# f.write("\nHello, I am a master in python programming.")
# f.close()
# f=open("demo.txt")
# print(f.read())

# f=open("demo.txt","x")

# import os
# os.remove("demo.txt")
