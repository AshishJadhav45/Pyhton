from datetime import date

from dateTime import date
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    @classmethod
    def details(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def check_age(age):
        return age > 18
#driver's code
p1 = Person('virat' , 20)
p2 = Person.details('Anushka' , 2002)
print(p1.name, p1.age)
print(p2.name,p2.age) 

print(Person.check_age(0))