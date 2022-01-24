# In one of your previous lessons, you have written a program called  "Guess the number" game by pre assigning the number to be guessed.
# Python provides a built-in module that you can use to generate random numbers.
# Let's take a look. 
'''Task 1: It's all Random'''
print("***** Task 1: *****")
print()
# Uncomment the statements below and click Run

import random
# num=int(input("Guess a number between 0 and 10: "))
# if num==random.randrange(0, 11):
#  print("You guessed the right number")
# else:
#  print("Sorry! Better luck next time") 

# We have imported the module random and have used the function random.randrange(0, 11) to generate a number between 0 and 11. 
# Here the function randrange() returns a number between 0 (included) and 11 (not included)

'''Task 2:  Password Generator'''
print("***** Task 2: *****")
print()
# The random module can also return a random element from a given string.
# Uncomment the statements below, click Run and observe the output

# y="python"
# import string
# lower_upper_alphabet = string.ascii_letters
# print(lower_upper_alphabet)
# val=random.choice(lower_upper_alphabet)
# print(val)

# Run the program 3 to 4 times and see the output changing.
# choice() shuffles the character in the string and returns random character each time.
# The choice()  function can be used in applications that require a random Ready to write a program that generates a random password. Part of the program is written for you..
# Uncomment the statements, complete the program and click Run, to execute the program
# import random
# passw=""
# x="welcome"
# y="CODING"
# z="123456"
# #Complete the program using for loop password to be generated.
# for i in range(3):
#   p=random.choice(x)
#   c=random.choice(y)
#   b=random.choice(z)
#   passw=passw+p+c+b
# print(passw)  

'''Task 3: Volfsball pitch'''
print("***** Task 3: *****")
print()
# Your friend wants to create a Volfsball pitch.
# Write a program that generates a random number between 10m and 15m. This number will be used as the radius to find the area and circumference. 
# The area and circumference value will be used to create a Volfsball pitch.
# Hint: Area of circle = 3.14*radius*radius
#       Perimeter of a circle= 2*3.14*radius

num=random.randrange(10, 16)
print("The radius of the Volfsball pitch is:",num)
area=(num**2)*3.14
circumference=(num*2)*3.14
print("\nThe area of the Volfsball pitch would be:",area)
print("\nThe circumference of the Volfsball pitch is:",circumference)

'''Fantastic!! You are getting better with working with the “random” package/module . Way to go!!'''