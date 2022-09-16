'''num1 = float(input("Enter a number :"))
op = input ("Enter a operator :")
num2 = float(input("Enter a number :"))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Envalid operator")             

# simple calcy
num1 = float(input("Enter a number "))
op  = input("Enter a operator")
num2 = float(input("Enter a second number"))


if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid operator")



# This is list

Friendcirle = {
 
 "Sam": "Alisha",
 "Mona": "Siddhi",
 "Gana": "Shital",
 "Susu": "Shweta",
 "Aksh": "Fugi",
 "Ash": "Single",
 "Sonya": "Single",
 "Omkar": "Invalid",
 "Akshay": "Single"
 }


print(Friendcirle.get("Ash"))

secrets_word = "rohit"
guess = ""

while guess != secrets_word:
    guess = input("Enter a guess :")
print("Congrats you guess right ")    



# Getting input from to the  user

name = input("Enter your name")
age = input("Enter your age")
college = input("Enter your college name")
hair_color = input("Enter your hair color")

print ("Hello"+name, "so you are"+age,"you complete your study in "+college , "so you have" + hair_color )



# simple calcy

num1 = float(input("Enter a Number"))
op = input("Enter a operator")
num2 = float(input("Enter a Second Number"))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1 + num2)
elif op == "*":
    print(num1*num2)
else: 
    print("invalid operator")


# Dictionaries 
friendcirle ={
    "sam" : "Alisha",
    "mona": "Siddhi",
    "haggy": "Shweta",
    "ash": "Single"
}

print(friendcirle.get("mona"))

# Simple Calculator 

num1 = float(input("Enter a number :"))
op = input("Enter a operator :")
num2 = float (input("Enter a second number :"))

if op ==  "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1+num2)    
elif op == "/":
    print(num1/num2)
else:
    print("Invalid Syntax")


# Dictionaries

friendcicle = {

    "sam" : "alisha",
    "monesh" : "siddhi",
    "haggy" : "shweta",
    "ash": "sigle"

}

print(friendcicle.get("sam"))

import secrets

secrets_world = "Ash"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secrets_world and  not (out_of_guesses):
 if guess_count < guess_limit:
    guess = input("Enter Guess :")
    guess_count += 1


if out_of_guesses:
    print("Out of guesses , you losses")

else:
     out_of_guesses = True
print("You win")



#for loop
friends = ["kohli","rohit","rahul"]

for index in range (5):
    print("friends[index]")

# exponent data
def raise_to_power(base_name,pow_num):
    result = 1
    for index in range (pow_num):
      result = result * base_name
    return result

print(raise_to_power(2,3))
    
#2d list and nested loop


formula = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in formula:
    for col in row:
        print(c)





try:
    value = 10/0
    number = int(input("Enter a Number :"))
    print(number)


except  ZeroDivisionError as err:
    print("Diveded by zero")
except ValueError:
    print("Invalid input")
'''


#file read 

# to make easy calcy
#Dictionaries
# Number Guess 

    
