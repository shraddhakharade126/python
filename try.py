# x=10
# try:
#     print(x)
# except:
#     print("Try again")
# else:
#     print("Welcome try does not occur error")
# finally:
#     print("run sucessfully")

try:
   f=open("file.txt")
except FileNotFoundError:
    print("File not found")
except NameError:
    print("Name error")


try:
    print(x)
except Exception as e:
    print(e)

