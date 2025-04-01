#this format use to open(read) file
'''file =open("harry.txt", "r")  #(harry.txt) file name
x=file.read()
print(x)
file.close()   #f.close() defalt parameter user use
'''

#this is a write file method
'''f = open("p.txt", "w")
f.write("this is nice")
f.close()'''


# this method use to write file "with function" /  # f.close not need with function 
'''
with open('example.txt', 'w') as file:
    file.write('Hello, this is a new line of text in the file!\n')
    file.write('This is another line of text.')

print("File written successfully.")''' #user satisfied program exit

# with open('prince.txt', 'w') as file:
#     file.write('jay ho')
#     print("mm")


# a(appened mthod) appened method means add value
'''st = "hello"
f= open("p.txt","a")
f.write(st)
f.close()'''

