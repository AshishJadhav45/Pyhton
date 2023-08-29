smallest = None

for value in [22,3,45,6,2,55,65,1]:
    if smallest is None:
        smallest = value
    elif value < smallest :
        smallest = value 
        print(smallest)
print("smallest number is", smallest)

