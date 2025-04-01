#super method with single inheritance
'''class ceo:
    name="prince"
    salary=10000000
    def show(self):
        print(f"{self.name} and {self.salary}")

class employee(ceo):
   
    def print(self):
        super().show()
        # print(f"name is : {self.name} and salary is : {self.salary}")

a=ceo()
b=employee()
b.show()
b.print()'''



#super method with multipal inheritance
'''class empolyee :
    name="prince"
    company="PR5"  
    def show(self):
        print(f"name is : {self.name} and company name is : {self.company}")


class programer :
    lastname="bhatt"
    othercompany="zzz"
    def print(self):
        print(f"last name is : {self.lastname} and other company name is :{self.othercompany}")


class coder( programer,empolyee):
    def show(self):
        super().show()   #when use super() method, not a use next line 
        print("hi")
        super().print()
        # print(f"name is : {self.name}, company name is : {self.company},last name: {self.lastname} and othercompany name: {self.othercompany}")
       


a=empolyee()
b=programer()

c=coder()
c.show()'''



#super method with mutilevel inheritance

'''class empolyee:
    name ="prince"
    position="CEO"
    def show(self):
        print(f"name is : {self.name} and  position is : {self.position}")


class programer(empolyee):
    company ="pr5"
    def show(self):
        print(f"company name is : {self.company}")


class coder (programer):
    other ="xyz"
    def show (self):
        super().show()
        # print(f"other : {self.other} ,name is : {self.name} , position is : {self.position} and company name is : {self.company} ")


a=empolyee()
b=programer()
c=coder()
c.show()'''