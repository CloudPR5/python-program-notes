"""a spam comment is defiend as a text containing following keywords:
'make a lot of money ' ,'buy now ',subscribethis','click this' .
write a progam to detect these spams"""

p1="make a lot of money"
p2="buy now"
p3="subuscribe this"
p4="click this"

message=input("enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is a message spaam", message)

else:
    print("this comment not a spam", message)