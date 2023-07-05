with open('python.txt' , 'r') as f :
    f.seek(10)


    data = f.read(5)
    print(f.tell()) # this is used for what postion of your words

    print(data)


# Anonymous function program
mac = lambda x : x*2

print(mac(2
))

#write a  code for adding two number

a = 4
b = 5
print(a+b)