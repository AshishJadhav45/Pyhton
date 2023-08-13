def factorial(x): # Defining a function to calculate factorial
if x == 1: # Base case
print("Factorial of 1 is 1")
return 1
else: # Recursive case
print("Factorial of",x," is ",(x * factorial(x-1))) # Recursive call
return (x * factorial(x-1))

for _ in range(int(input("Number of Test cases: "))): # Main function
print("Factorial = ",factorial(int(input("Enter number: ")))) # Calling the function

def main(): # Main function
print("Factorial = ",factorial(int(input("Enter number: ")))) # Calling the function

if __name__ == "__main__": # Driver code
main()
