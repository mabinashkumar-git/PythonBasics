# Syntax -> class Classname: -> Press one enter then in next line cursor should come with some gap i.e. not from starting of line, then this denotes
#                               whatever line you will be writing now will come under class, like in java writing code inside {} but if you move cursor
#                               to starting then codes written will be determined as writen outside class.
#                               Similar indentation goes for writing methods
# Syntax in Java -> public class Classname {}, public void methodName(){}

def MethodName():
    print("Inside Method")
print("Outside Method")

MethodName()   #Function is called from here

print ("********************* 1 **************************")

def MethodName1(name):              #parameterizing
    print("Inside Method1", name)
    print("Inside Method1" + name)

MethodName1("Abinash Mallick")

print ("********************** 2 ************************")

def AddIntegers(a, b):
    sum = a + b
    print("Sum:",sum)

AddIntegers(7,8)
