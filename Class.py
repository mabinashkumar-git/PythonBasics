# Syntax -> class Classname: -> Press one enter then in next line cursor should come with some gap i.e. not from starting of line, then this denotes
#                               whatever line you will be writing now will come under class, like in java writing code inside {} but if you move cursor
#                               to starting then codes written will be determined as writen outside class.
#                               Similar indentation goes for writing methods
# Syntax in Java -> public class Classname {}, public void methodName(){}


class Calculator:
    num = 70
    print("Inside Class")

    def getData(self):
        print("Inside getData method")

obj = Calculator() #Syntax to create object in python Objectname = Classname
print(obj.getData())
print(obj.num)