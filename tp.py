'''
# Argument

def my_function(str1,str2):
  print(str1)
  print(str2)
my_function("hello this is first line 1","This is second line 2") 
my_function(55,88) 
my_function("hey there my name is tesla and i'm a driverless car","Also call me Autopilot")

# Default Argument

def yourself(name="someone" , age = "Unkhown"):
  print("Hello my name is " , name, "and my age is " , age)

yourself ("mahi")  

# keyword Argument
yourself(name= "virat" , age=45)




def cricket(*cricketers):
  for man in cricketers:
    print("hey this is ", man)

cricket("Rohit","Rahul","Virat","Hardik","Rishabh","SKY","Hooda","jasprit","Arshdip","Bhuvi","Chahal","Ashvin")


def do_math(num1,num2):
  return num1+num2

math1 = do_math(53,44)
math2 = do_math(55,555)

print("first sum is",math1,"and second is ",math2)


def sam(num1 ,num2):
  return num1 * num2

math3 = sam(45,2)
math4 = sam(5,5)

print("The first multiply is" ,math3 ,"and second multiply", math4)

'''



name = input("Enter a favorite cricketer name :")

if name == "virat":
  print(" i'm a virat 18")
elif name == "Rohit":
  print("Hey Rohit here 45")
elif name == "Rahul":
  print("I'm Rahul 1 ")
elif name== "jaddu":
  print("Hello jaddu here 33")      
else:
  print("is not a cricketer")  
































