def palindrom():
    num=int(input("enter number "))
    rem=0
    sum=0
    temp=num
    while num>0:
        rem=num%10
        sum=(sum*10)+rem
        num=int(num/10)
    if temp==sum:
        print("number is palindrom")
    else:
        print("Number is not palindrom")
palindrom()
