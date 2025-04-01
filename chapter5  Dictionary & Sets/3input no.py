#write a program to input eight number from the user and display all the unique numbers(once)

s=set()
number=input("enter number 1:")
s.add(int(number))

number=input("enter number 2:")
s.add(int(number))

number=input("enter number 3:")
s.add(int(number))

number=input("enter number 4:")
s.add(int(number))

number=input("enter number 5:")
s.add(int(number))

number=input("enter number 6:")
s.add(int(number))

number=input("enter number 7:")
s.add(int(number))

number=input("enter number 8:")
s.add(int(number))

print(s)
print("type of set:" , type(s))
