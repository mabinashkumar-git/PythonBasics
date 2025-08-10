

class Calculator:
    num = 70
    print("Inside Class")

    def __init__(self,a,b):  #Constructor creation. Constructor name should always be innit unlike Java same as classname
        self.a = a
        self.b = b
        print("Constructor is called automatically",a,b)

    def getData(self):
        print("Inside getData method")

    def sum(self):
        print(self.a + self.b + Calculator.num)
        print(self.a + self.b + self.num)

        return self.a + self.b

#Here all the below codes will be determined as written outside class, as it starts from staring of line and do not follow indentation of class

obj = Calculator(2,3) #Syntax to create object in python Objectname = Classname, new keyword is not req as Java for obj creation
print(obj.__init__(12,13))
print(obj.getData())
print(obj.num)
print(obj.sum())

# print(obj.__init__(20,30))
# print(obj.getData())
# print(obj.num)
# print(obj.sum())
