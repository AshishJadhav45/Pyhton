# # find out the smallest number from the list 


smallest = None 

for value in [11,22,3,44,2,55,1]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest)

print('the smallest number is ', smallest)

























