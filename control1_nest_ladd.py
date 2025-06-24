num1=int(input("Enter number :"))
num2=int(input("Enter number :"))
num3=int(input("Enter number :"))
if num1>num2:
    if num1>num3:
        print(num1,"is max")
    else:
        print(num3,"is max in case 1")
else:
    if num2>num3:
        print(num2,"is max")
    else:
        print(num3, "is max in case 2")