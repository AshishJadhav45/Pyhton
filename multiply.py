for _ in range(int(input("Enter number of Test cases:"))):
n = int(input("Enter a number:"))
print(*[n*i for i in range(1,11)])