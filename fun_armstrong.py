def arm_strong():
    num=int(input("Enter number "))
    rem=0
    temp=num
    sum=0
    while  num>0:
        rem=num%10 
        sum+=(rem*rem*rem)
        num=int(num/10)
        print(sum)
    if temp==sum:
        print("number is arm strong")
    else:
        print("number is not arm strong")

arm_strong()



















































































