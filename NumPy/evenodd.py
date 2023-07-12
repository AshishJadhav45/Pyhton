import math
def is_prime(n):

    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for _ in range(int(input("Number of Testcases: "))):
    n = int(input("Enter number:"))
    print("Even" if n%2==0 else "Odd")
    print("Prime" if is_prime(n) else "Not-Prime")