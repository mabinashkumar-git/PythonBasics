from Constructors import Calculator


class ChildClass(Calculator):  #Here Parent class is inherited to child class by  mentioning the parent class name inside bracket of child Classname
                               # unlike extends keywords like Java
    number = 300

    def __init__(self):
        Calculator.__init__(self,20,90)

    def getAllData(self):
        return self.number + self.num + self.sum()

Object = ChildClass()
print(Object.getAllData())