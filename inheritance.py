class employee:
    def __init__(self , name , id):
     self.name = name
     self.id = id
    def info(self):

        print(f"Name of the employee is {self.name} and his id is {self.id}")

class programmer(employee):
    def showlanguage(self):
        print("python")
    
class manager(employee):
    def showlanguage(self):
        print("c++")
    
e = employee("sachin" , 420)
e.info()
e2 = programmer("shubham" , 340)
e2.info()
e3 = manager("saurabh" , 420)
e3.info()