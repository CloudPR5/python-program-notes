#write a program to find the greatest of four numbers entered by the user.

a1= int(input("enter the value 1:"))
a2= int(input("enter the value 2:"))
a3= int(input("enter the value 3:"))
a4= int(input("enter the value 4:"))


if (a1>a2 and a1>a3 and a1>a4):
    print("greatest number is:",a1)

elif (a2>a1 and a2>a3 and a2>a4):
    print("greatest number is:",a2)

elif (a3>a1 and a3>a3 and a3>a4):
    print("greatest number is:",a3)
    
else:
    print("greatest number is:",a4)

# if(a>=10):
#     print("greastest")

# elif(a<=0):
#     print("error")
# else:
#      print("lowest")

#      print("end of program")