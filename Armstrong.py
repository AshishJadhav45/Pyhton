def armstrong(number):
    num = str(number)
    power = len(num)
    digit_sum = sum(int(digit)** power for digit in num )
    return number == digit_sum

number = int(input("Enter a number:"))

if armstrong(number):
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is not a armstrong number!")