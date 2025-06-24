def digit():
    num=int(input("Enter number "))
    rem=0
    while num>0:
        rem=num%10
        print(rem)
        num=int(num/10)
digit()