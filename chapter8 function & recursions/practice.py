
'''#function difination
def avg():
    a= int(input("Enter a number:"))
    b= int(input("Enter a number:"))
    c= int(input("Enter a number:"))
    average=(a+b+c)/3
    print(average)

#function call
avg()
print("thank you")

avg()
print("thank you")

avg()
print("thank you")'''


'''def avg():
    a= input("Enter a string:")

avg()
print("Good day")'''


#write a program to great a user with"Good day" using function
'''def goodday():
    print("good day")

    goodday()'''

#function with arrduments
'''def goodday(name):
    print("good day," + name)
   
    return "done"

a=goodday("prince")
print(a)
'''
#Default parameter value
def goodday(name, ending="thank you"):
    print(f"good day, {name}")
    print(ending)
   
    return "done"

a=goodday("prince", "thanks")  #not a set defalt value
goodday("hello")  #defalt value set thank you
print(a)