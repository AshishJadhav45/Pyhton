#Some Math

#Program no 1
#Write a program that will multiply the sum of 5 and 6 by 57.3 and output the result.

print((5+6)*57.3)

#Program no 2
#Write code to output 4 raised to the 5th power.
# output Expected 1024

print(2**10)

#Program no 3

# Calculate and output the total flight time in hours
'''
Flight Time
You need to calculate the flight time of an upcoming trip.
You are flying from LA to Sydney, covering a distance of 7425 miles,
the plane flies at an average speed of 550 miles an hour.
Calculate and output the total flight time in hours.'''

#given # distance = 7425 miles
       # average speed = 550 miles in hours
print(7425/550)      


#Program no 4
#Write a program to output the letters A B C D, each on a separate line.
print("A\nB\nC\nD")

#Program no 5
'''
You’re given a task to write the word "hi" 42 times. Boring, right?
Write a program to do it for you.
Create a program to output "hi" 42 times, without any separators, on the same line
'''
print("hi"*42)

#Program no 6
# String Program
'''
You need to make a program for a leaderboard.
The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
1.
2.
3.
...
'''
# print("1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.")

print(20//9)

'''
Program no. 7

When you go out to eat, you always tip 20% of the bill amount. But who’s got the time to calculate the right tip amount every time? 
Not you that’s for sure! You’re making a program to calculate tips and save some time.
Your program needs to take the bill amount as input and output the tip as a float

'''
bill = int(input())
tip = 20/100 * bill
print(float(tip))

'''
Program no.8
Write a program that checks if the water is boiling.
Take the integer temperature in Celsius as 
input and output "Boiling" if the temperature is above or equal to 100.
'''

temp = int(input("Enter"))

if temp >= 100:
       print("Boiling")

'''
Program no. 9
Write a program to control entrance to a club.
Only people who are 18 or older are allowed to enter the club.
Your program takes the age of the person who tries to enter, and outputs "Allowed"
if they are allowed to enter the club,
and "Sorry" if they are younger than the allowed age.

'''
age = int(input("Enter your age :"))
if age>18:
       print("Allowed")
else:
       print("Sorry") 

'''
Program no. 10
Given the age of a person as an input, output their age group.

Here are the age groups you need to handle:
Child: 0 to 11
Teen: 12 to 17
Adult: 18 to 64

'''             

age = int(input("Enter a age :"))

if age > 0 and age< 11:
       print("Child")
elif age >= 12 and age<= 17:
       print("Teen")
elif age >= 18 and age <= 64:
       print("Adult")              



'''
Program no.11

You are given a program that outputs all the numbers from 0 to 10.
Change the code to make it output only the even numbers.'''       

x = 0
while x <=10:
       if x%2==0:
              print(x)
       x += 1       

'''

Program no.12
for Loops

for loops allow you to easily iterate through lists.

Given a list of numbers, calculate their sum using a for loop.       

'''

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
sum = 0
for num in x:
    sum += num
print(sum)


'''
Problem no.13

Ranges


You are creating a date picker for a website and need to output all of the years in a given period.
Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.
The output sequence should start with the first input number and end with the second input number, without including it.

Sample Input
2005
2011

Sample Output
[2005, 2006, 2007, 2008, 2009, 2010]




'''
# solulation

a = int(input())
b = int(input())

list = list(range(a,b))
print(list)

'''
Problem no.14

List Slices


Write a program that takes a string as 
input and outputs the last character of that string.
'''

str = input()
print(str[-1])


'''#Problem no .15

Sum of Consecutive Numbers


No one likes homework, but your math teacher has given you an assignment
 to find the sum of the first N numbers.

Let’s save some time by creating a program to do the calculation for you!

Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input
100

Sample Output
5050

Explanation: The sum of all numbers from 1 to 100 is equal to 5050.

'''

# solution
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

'''
# Problem no.16

Your friend sent you a message, however his keyboard is broken and types a # instead of a space.

Replace all of the # characters in the given input with spaces and output the result.

'''
#solution

msg = input()

msg = msg.replace("x" , " ")
print(msg)


# Problem no 17

'''
Arguments


The given program defines a function printBill(),
 which takes one string argument and outputs formatted text.
You need to take the user input and call the function by
 passing the input as its argument.

'''
#solution
def printBill(text):
  print("======")
  print(text)
  print("======")


text = input()
printBill(text)


# problem no . 18
"""
Search Engine


You’re working on a search engine. Watch your back Google!

The given code takes a text and a word as input and passes
 them to a function called search().

The search() function should return "Word found" if the word is present in the text,
 or "Word not found", if it’s not."""

#solution
# search engine
def search(text, word):
    """Search engine"""
    # look whether the word is in the text provided
    if word in text:
        print('Word found')
    else:
        print('Word not found')

text = input()
word = input()
search(text, word)




