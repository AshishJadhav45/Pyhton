### list comprehension with conditional statement

print("List comprehension result:")

print([x for x in range (1,100) if x % 10 == 0])

print("Long form code result:")

my_list = []
for x in range (1,100):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)


