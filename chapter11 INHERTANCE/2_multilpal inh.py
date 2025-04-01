class empolyee :
    name="prince"
    company="PR5"  
    def show(self):
        print(f"name is : {self.name} and company name is : {self.company}")


class programer :
    lastname="bhatt"
    othercompany="zzz"
    def show (self):
        print(f"{self.name} and {self.company}")


class coder(empolyee, programer):
    def show(self):
         print(f"name is : {self.name}, company name is : {self.company},last name: {self.lastname} and othercompany name: {self.othercompany}")
       


a=empolyee()
b=programer()

c=coder()
c.show()

