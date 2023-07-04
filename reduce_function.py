from functools import reduce

# Create a list of numbers
number = [2,3,5,6,7]

# Use reduce to sum the numbers in the list
sum = reduce(lambda x,y: x + y , number)

# Print the sum
print(sum)