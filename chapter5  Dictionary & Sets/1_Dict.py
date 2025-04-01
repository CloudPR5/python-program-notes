a={
    "key":100,
    "shubham":56,
    "rohan":23

}

print(a) # main dict print
print(a["key"]) # one value print karane ke liye

print(type(a)) # value print type 

print(a.items()) #all function print

print(a.update()) #as it write find none value

a.update({"key":99}) # this method use changes & add other value main dict
print(a)

print(a.git("key"))  # print none

print(a["key"]) # Returns an error