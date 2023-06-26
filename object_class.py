
# Define a class called person.
class person:
    # Define attributes for the class.
    name = "sachin"
    occupation = "Cricketer"
    runs = 10000

    # Define a method for the class.
    def info(self):
        print(f"{self.name} is a {self.occupation} and he has scored {self.runs}")

# Create instances of the class.
a = person()
b = person()
c = person()

# Add attributes to the instances.
a.name = "virat"
a.occupation = "one down batsman"
a.runs = 12000

b.name = "rohit"
b.occupation = "opener"
b.runs = 8000

c.name = "dhoni"
c.occupation = "finisher"
c.runs = 5000

# Call the method for each instance.
a.info()
b.info()
c.info()