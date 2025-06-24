# def oddeven():
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         return "The number is even"
#     else:
#         return "The number is odd"
# result=oddeven()
# print(result)
# print("The number is even") if oddeven() == "The number is even"

def leapyear():
    year = int(input("Enter a year: "))
    if year % 4 == 0 :
        if year % 100 == 0:
            if year % 400 == 0:
                return "The year is a leap year"
            else:
                return "The year is not a leap year"
        else:
          return "The year is a leap year"
    else:
       return "The year is not a leap year"
result=leapyear()
print(result)