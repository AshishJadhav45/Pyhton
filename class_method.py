# Define a class called Employee
class Employee:

    # Define the company attribute
    company = "Apple"
    
    # Define the show method
    def show(self):
        print(f"The name is {self.name } and company is {self.company}")

    # Define the changecompany method
    @classmethod
    def changecompany(cls, newcompany):
        cls.company = newcompany

# Create an instance of the Employee class
e1 = Employee()

# Set the name attribute of the Employee class
e1.name = "sachin"

# Call the show method
e1.show()

# Call the changecompany method
e1.changecompany("Google")

# Call the show method
e1.show()

# Print the company attribute
print(Employee.company)