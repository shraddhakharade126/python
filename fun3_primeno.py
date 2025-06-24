def primeno(num):
    cnt=2
    while cnt<=num:
        if num%cnt==0:
            break
        cnt+=1
    if cnt==num:
        return "number is prime"
    else:
        return "number is not prime"
num=int(input("Enter number "))
print(primeno(num))