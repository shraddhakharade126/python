def power_cal():
    num=int(input("Enter number "))
    p=int(input("enter power "))
    sum=1
    while p>0:
        sum*=num
        p-=1
    print(sum)
power_cal()