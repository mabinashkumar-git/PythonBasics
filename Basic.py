# https://journaldev.com/14036/python-data-types

#syntax to print in python
print("hello")

# declaring  variables
a = 3
print(a)

#Assigining/Declaring a variable
name = "demo"
print(name)

#Assigining/Declaring multiple variable
b, c, d = 5,6.4, "great"
print(b, c, d)
print("value is",b)

print("{} {}".format("Value is  :",b))

# type keyword in Python determines type of data type used
print(type(b))
print(type(c))
print(type(d))


e,f, g = 100, 10.2345, 100+3j
print("Variable type of ", e, "is ", type(e))
print("Variable type of ", e, "is ", type(f))
print("Variable type of ", e, "is ", type(g))


a = "I am first"
b = "I am second"
print(a, "concate with", b)

# plus symbol can be used in print statement when we concate two strings
print(a + " concate with " + b)