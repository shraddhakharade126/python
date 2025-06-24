# class Evenodd:
#     def __init__(self):
#         self.num=int(input("Enter number "))
#     def display(self):
#         if self.num%2==0:
#             print("number is even")
#         else:
#             print("number is odd ")

# obj=Evenodd()
# obj.display()

class Evenodd:
    def __init__(self,num):
        self.num=num
    def display(self):
        if self.num%2==0:
            print("number is even")
        else:
            print("number is odd ")

num=int(input("Enter number "))
obj=Evenodd(num)
obj.display()

