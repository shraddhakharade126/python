def simple():
    p=float(input("Enter p amount "))
    n=float(input("Enter no of year's "))
    r=float(input("Enter rate of interest "))
    amount=(p*n*r)/100
    return amount
amount=simple()
print("Amount :",amount)