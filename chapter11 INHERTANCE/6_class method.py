#@class method 
"""without useing @classmethod"""
class employee:
    a=2

    # this function use to print the modified value
    def show(self):
        print(f"value is : {self.a}") # this function use to print the modified value


x= employee()
x.a=50
x.show()       #normal inheritence without using @classmethod 




""""with using @classmetod"""
class employee:
    a=2


    # print the original value 
    @classmethod
    def show(cls):
        print(f"value is : {cls.a}")  # print the original value 


x= employee()
x.a=50
x.show()       #normal inheritence with  using @classmethod