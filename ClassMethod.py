
class MyClass:

    @classmethod                #tag used for calling method without creating object of the class
    def class_method(cls):
        return "Class"

    def instanceMethod(self):
        return "Instance"

obj = MyClass()
print(obj.instanceMethod())
print(obj.class_method())

print(MyClass.class_method())   #calling method without creating object of the class
