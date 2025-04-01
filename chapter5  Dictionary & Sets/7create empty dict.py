'''create an empty dictonary.
allow 4 friends to enter thier favorite lunguage as 
value and use key as their names.
 assume that the names are unique.'''

d={}

name=input("enter friends name:")
lang=input("enter lunguage name:")
d.update({name:lang})

name=input("enter friends name:")
lang=input("enter lunguage name:")
d.update({name:lang})

name=input("enter friends name:")
lang=input("enter lunguage name:")
d.update({name:lang})

name=input("enter friends name:")
lang=input("enter lunguage name:")
d.update({name:lang})

print(d)