#single inhertance

#first program
'''class animal:
   def show(self):
      print("animal live in a forest")

class dog(animal):
   def speak(self):
      print("dog barks")


a=animal()
b=dog()

b = dog()
b.speak()
b.show()'''


# second f program
'''class animal:
   lives = "forest"
   name= "ani"
   def show(self):
      print(f"the lives in :{self.lives} and name of {self.name}")


class dog(animal):
   language = "love "
   def language(self):
      print(f"{self.language}")

a=animal()
b=dog()
b.show()
b.language()'''

'''# Example 3: Parent Class and Child Class with a Simple Method
class shape:
    def area(self):
        print("claculating area a shape "):

class circle(shape):
    def show(self):
        print("area of the circle is  π * r²"):

a=shape()
b=circle()
b.area()
b.show()'''


class ceo:
    name="prince"
    salary=10000000
    def show(self):
        print(f"{self.name} and {self.salary}")

class employee(ceo):
   
    def print(self):
        print(f"name is : {self.name} and salary is : {self.salary}")

a=ceo()
b=employee()
b.show()
b.print()