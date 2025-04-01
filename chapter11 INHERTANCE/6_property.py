class employee:
    a=2

    # this method use print the original value 
    @classmethod
    def show(cls):
        print(f"value is : {cls.a}")  # this method use print the original value 


    # this method use to print the ...

    """Getter: The @property decorator is used to define a method that acts like an attribute. It allows you to read the value of a private variable.

     Setter: Using @property_name.setter, you can define a setter method that validates or transforms the value before assigning it to the attribute.

     Encapsulation: property allows you to hide the internal representation of an attribute while exposing a clean interface for getting and setting it."""
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


#normal inheritence with  using @classmethod
x= employee()
x.a=50
x.show()       #normal inheritence with  using @classmethod



#using @propertymethod
x.name = "harry rodi"
print(x.name)
x.show()        #using @propertymethod