# # find out the largest number from the list 

# # first we initialize smallest number for comparassion 

first_number = 0

for numbers in [11,33,45,32,11,55,332,567,45]:
    if numbers > first_number:
        first_number = numbers
    print(numbers,first_number)

print("the largest number is ",first_number)










