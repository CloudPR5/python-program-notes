'''class Employee:
    language = "py"  #this is a class attribute
    salary = 1200000

harry = Employee()
harry.name="harry" #this is an object(instance) attribute
print(harry.name,harry.language, harry.salary)
'''

#when define saprit instance attributes
'''class Employee:
    language="python"  #this is a class attribute
    salary=120000

harry =Employee()
harry.language ="js" ##this is an object(instance) attribute
print(harry.language, harry.salary)
'''

# self function
'''class Employee:
    language="python"
    salary=1200000

    def gitinfo (self):
        print(F"the language is {self.language}.the salary is {self.salary}")
        
harry = Employee()
harry.language="js"
harry.gitinfo()   #harry.gitinfo()  or  Employee.gitinfo(harry) same 
# Employee.gitinfo(harry)'''

#dunder method

class Employee:
    language="python"
    salary=1200000

    def __init__(self):  #dunder method is automatically called(harry=Employee())
        print("i am create an object")

    def gitinfo (self):
        print(F"the language is {self.language}.the salary is {self.salary}")
        
harry = Employee()
harry.language="js"
harry.gitinfo()   #harry.gitinfo()  or  Employee.gitinfo(harry) same 
# Employee.gitinfo(harry)
