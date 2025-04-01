#super method with mutilevel inheritance

class empolyee:
    name ="prince"
    position="CEO"
    def show(self):
        print(f"name is : {self.name} and  position is : {self.position}")


class programer(empolyee):
    company ="pr5"
    def print(self):
        print(f"company name is : {self.company}")


class coder (programer):
    other ="xyz"
    def show (self):
        super().show()
        super().print()
        print(f"other : {self.other}")
        # print(f"other : {self.other} ,name is : {self.name} , position is : {self.position} and company name is : {self.company} ")


a=empolyee()
b=programer()
c=coder()
c.show()