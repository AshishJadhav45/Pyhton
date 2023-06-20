class Person:
    name = "John" #name is a string variable that is set to "John"
    occupation = "Software Engineer" #occupation is a string variable that is set to "Software Engineer"
    networth = 1000000 #networth is a numerical variable that is set to 1000000
    def info(self): #info is a method that prints the name and occupation of the person
        print(f"{self.name} is a {self.occupation}") #this line prints the name and occupation of the person

a = Person() #a is an instance of Person
b = Person() #b is an instance of Person
c = Person() #c is an instance of Person
d = Person() #d is an instance of Person


a.name = 'shubham' #the name of a is set to "shubham"
a.occupation = 'student' #the occupation of a is set to "student"

b.name = 'saurabh' #the name of b is set to "saurabh"
b.occupation = 'HR' #the occupation of b is set to "HR"

c.name = 'sagar' #the name of c is set to "sagar"
c.occupation = 'manager' #the occupation of c is set to "manager"

d.name = 'sachin' #the name of d is set to "sachin"
d.occupation = 'CEO' #the occupation of d is set to "CEO"

a.info() #this prints the name and occupation of a
b.info() #this prints the name and occupation of b
c.info() #this prints the name and occupation of c
d.info() #this prints the name and occupation of d