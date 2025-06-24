
class rev_str:
    def revprint(self,str1):
        ls=str1.split(" ")
        print(ls[::-1])
        return
str=input("enter string :")
s=rev_str()
s.revprint(str)
