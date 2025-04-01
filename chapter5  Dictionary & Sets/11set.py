e=set()  # this is empty set 
e=set # not empty set
print(e)
print("e:", e)
print("type of set:" , type(e))

if not e:
    print("The set is now empty.")
else:
    print("The set is not empty.")


# s={1,2,3,4,5,66,66,88,88,2,3} # set cannot contain duplicate values
# print(s)  #{1, 2, 3, 4, 5, 66, 88} output
# s.add(99)  #random value add 

# print(s)


# #intersection & union
# s1={2,3,5,8,4,6}
# s2={2,5,9,8,6,12}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1-s2)
# print(s1+s2) #return error
