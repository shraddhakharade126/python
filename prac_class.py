# class Greater:
#     def getdata(self):               
#         self.num1=int(input("Enter number 1 "))
#         self.num2=int(input("Enter number 2 "))
#     def display(self):
#         if self.num1>self.num2:
#             print(self.num1 ," is greater")
#         else:
#             print(self.num2 ," is greater")

# obj=Greater()
# obj.getdata()
# obj.display()

# class factorial:
#     def getdata(self):
#         self.num=int(input("Enter number :"))
#     def display(self):
#         self.fact=1
#         for i in range(1,self.num+1):
#             self.fact*=i
#         print("Factorial :",self.fact)

# f=factorial()
# f.getdata()
# f.display()


# class pos_neg:
#      def getdata(self,num):
#         self.num=num
#      def display(self):
#             if self.num>0:
#                 print("number is positive")
#             elif self.num==0:
#                 print("number is nutral")
#             else:
#                 print("number is negative")

# num=int(input("Enter number :"))
# obj=pos_neg()
# obj.getdata(num)
# obj.display()

class prime:
    def getdata(self,num):
        self.num=num
    def display(self):
        self.cnt=2
        i=0
        while self.cnt<=self.num:
            if self.num%self.cnt==0:
                break
            self.cnt+=1
        if self.cnt==self.num:
            print("number is prime ")
        else:
            print("number is not prime")

obj=prime()
obj.getdata(22)
obj.display()