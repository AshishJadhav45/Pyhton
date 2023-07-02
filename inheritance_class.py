class Company():
    def __init__(self, name , id):
        self.name = name 
        self.id = id

    def info(self):
        print(f"The Company name is {self.name} and id is {self.id}")
    
    def car(self):
        print(f"the workers works at {self.name} is {self.id} ")

class employee(Company):
    def car(self):
        print("Elon")

class workers(Company):
    def p(self):
        pritn("workers")


c = Company("Tesla", 302)
c.info()

model = employee("Tesla model", 5)
model.info()

workers = workers("Tesla" , 456)
workers.car()