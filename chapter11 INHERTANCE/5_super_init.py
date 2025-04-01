#super method with mutilevel inheritance

class empolyee:
    name ="prince"
    position="CEO"
    def __init__(self):
        print(f"name is : {self.name} and  position is : {self.position}")


class programer(empolyee):
    company ="pr5"
    def __inti__(self):
        print(f"company name is : {self.company}")


class coder (programer):
    other ="xyz"
    def __inti__(self):
        super().__init__()
        
        # print(f"other : {self.other}")
        # print(f"other : {self.other} ,name is : {self.name} , position is : {self.position} and company name is : {self.company} ")


a=empolyee()
b=programer()
c=coder()
# c.__init__()
print(b.company)
print(c.other)