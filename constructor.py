# constructer is a special method in python
# it is used to initialize the object
# it is called automatically when the object is created
# it is also called as init method
# it is used to initialize the instance variables
# it is used to initialize the instance variables with some default values
# it is used to initialize the instance variables with some user defined values

class person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def info(self):
        print(f"{self.name} is {self.age} years old")

a = person("sachin", 45)
b = person("virat", 32)

a.info()
b.info()