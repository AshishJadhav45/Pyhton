with open('python.txt' , 'r') as f :
    f.seek(10)

    # here we are reading 5 words from 10 postion
    data = f.read(5)

    # this is used for what postion of your words
    print(f.tell()) 

    # this is used for print your data
    print(data)


