

print ("                _______                ______    ______            _______           _____            ")
print ("  |    |        |     |   \      /    |          |     |   \   /      |     |     | |     |  |\   |   ")
print ("  |    |        |     |    \    /     |____      |_____|    \ /       |     |_____| |     |  | \  |   ")
print ("  |    |        |     |     \  /      |          |           |        |     |     | |     |  |  \ |   ")
print ("  |    |____    |_____|      \/       |______    |           |        |     |     | |_____|  |   \|   ")



# Variable and data 

character_name = "Ash"

character_age = "20"
is_Male = True
print("There once was a man named " + character_name +" ")
print("He was " + character_age + " years old")

character_name = "Sak"
print("He really liked the " +character_name+"")
print("But didn't like being " + character_age +".")


# String

print("Hello Ashish")

# 2nd example of String

ash = ("Jadhav ashish")
print(ash.upper().isupper()) #This is for upper case and tue or face 
print(len(ash))              #This is for lenth of string
print(ash[0:6])              #position
print(ash.index("s"))        #index of String
print(ash.replace("ashish","Sumit"))   #Replace the value




# Working with numbers

print(65+45)
print(3*(5+5))
print(10%3)

#2nd example of numbers

my_number = 45
print(my_number)

my_num = -5     # this is absulute value of number
print(abs(my_num))

#power of number
print(pow(4, 6))

my_num = (5,7,8,9)
print(max(my_num))
print(min(my_num))

from math import *

print(sqrt(100))


# Getting input from users

name = input("Enter your Name: ")
age = input("Enter your age :")
college = input("Enter your college name ")
hair = input("Enter your hair colour ")
status = input("Enter your status ")

print("Hello " + name +  " ! you are " +age + " your college name is "+college + " your hair colour is " +hair+ " you have a " +status) 



# building a basic calculator

num1 = input("Enter a Number :")
num2 = input("Enter a another Number : ")

result = float(num1) + float(num2)

print(result)

# mad libs games

color = input ("Enter a color : ")
plural_noun = input ("Enter a plural Noun : ")
celebrity = input ("Enter a celebrity : ")

print("Roses are " + color)
print(plural_noun+ " are blue")
print("i love "+ celebrity)

#List

friends = ["Mahi","Ishan","Rahul","Rohit","Virat"]
print(friends)
print(friends[2])         #position print the name
friends[0] = "Hardik"   #replace a name
print(friends)



#list function

lucky_number = [4,6,88,484,3485,18,6485613,84,56654]
friend = ["virat","rohit","rahul","hardik"]
friend.reverse()
friend.sort()
print(friend)
lucky_number.sort()
print(lucky_number)

#Tuples

#tupes are immutable 
#does not asign any value 

coordinates = (5,6) 
print(coordinates)


#function

def say_hi(name,age):
    print("Hello "+name , "your are "+str(age))

say_hi("virat",18)
say_hi("Rohit",45)

#Return statement


def cube(num):
    return num*num*num
ash = cube(5)    
print(ash)


# if statement


is_male = False

if is_male:
    print("you arer a male")
else:
    print("you are not a male")


#2nd example of if statement

is_male = False
is_tall = False

if is_male and is_tall:
    print("you are a takk male")
else:
    print("you are either not male or not a tall")    



# If statement and comparision

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(5,2,6))



# Better calculator

num1 = float(input("Enter a number :"))
op = input("Enter a operator: ")       
num2 = float(input("Enter a second number"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
                  

# Dictionaries

Monthconverstion ={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "Octomber",
    "Nov": "November",
    "Dec": "December"


}

print(Monthconverstion.get("Jan"))
 
i = 1
while i <= 10:
    print(i)
    i += 1
print ("Done loop")    

# Building a Guessing game
import secrets

secrets_word = "Ash"
guess = ""

while guess != secrets_word:
    guess = input("Enter a guess :")
print("Congracts you guess right")    





# reading a text file

file = open("text.txt" , "r")
print(file.read())
file.close()

#this lines for creat a new txt file using program
file = open("text1.txt","w")
file.write("\n ash")
file.close()


# modules and pip

# pip is pakage mananger 

# classes and object

from Student import Student

student1 = Student ("Oscar","Accounting",3.1)
student2 = Student ("ash", "Business" ,3.8)

print(student2.on_honor_roll())

#example 2 

from Ash import Ash

teacher1 = Ash ("kushal","Psychology",30)
teacher2 = Ash ("Ritviz","python",40)

print(teacher2.Is_better())

from Teacher import Teacher

teach1 = Teacher ("ash","Psycho",43)
teach2 = Teacher ("sam","cleaver",60)

print(teach2.Is_Great())

#Example 3


from Music import Music 

musician1 = Music ("ash","good",50)
musician2 = Music ("gana", "better",46)

print(musician1.Is_Good())


# inheritance 

from Chef import Chef 
from Chinese import Chinese

myChef = Chef()
myChef.make_special_dish()
myChef.make_chiken()
myChef.make_salad()

yourChef = Chinese()
yourChef.make_chiken()
yourChef.make_chiken_65()
yourChef.make_fried_rice()




from Enterpronour import Enterpronour

Teacher = Enterpronour()

Teacher.make_teach_art()
Teacher.make_teach_math()
Teacher.make_teach_science()


# to find whether a number is even or odd

number=int(input("Enter any number :"))

if (number%2)==0:
    print(number,"is even number")
else:
    print(number, "is odd number")    





