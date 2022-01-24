# Mr.Funky has just gotten started with writing functions.  
# He has been wondering if a function can have a default value set.
# Ready to check it out.

''' Task 1:  Defaultors '''
print("***** Task 1: *****")
print()
# Uncomment the statements below and click Run.

# def func(x=1):
#  y0 = x+ 1
#  y1 = x * 3
#  y2 = y0 ** 3
#  print("Value of y0 is: ", y0)
#  print("Value of y1 is: ", y1)
#  print("Value of y2 is: ", y2)
# print("Values without arguments")
# func()
# print()
# print("Values with arguments")
# func(3)

# What did you observe? 
# You can specify a default value for an argument.
# Default value is the value a function takes as an argument, if no argument value is passed.  
# Why do you think it is a good practice to specify default value for an argument? 
# You can avert errors if default value is specified. 

''' Task 2: Max or Min '''
print("***** Task 2: *****")
print()
# Write a function that takes two numbers as the input 
# - Returns the higher of the two.
# - If both the numbers are equal, it returns 0
# Set a default value for the argument
# Hint : Use if-else in the function
# def higher_of_two_num(num1=1,num2=1):
#   if num1>num2:
#       return num1
#   elif num2>num1:
#       return num2   
#   else:
#     return 0
# num1=float(input("Write a number of your choice: "))   
# num2=float(input("Write another number of your choice: "))    
# the_higher=higher_of_two_num(num1,num2)        
# if the_higher==0:
#   print("Your numbers are equal")
# the_higher=higher_of_two_num(num1,num2)        
# print(the_higher,"is the biggest number of yours")

''' Task 3: Factorials '''
print("***** Task 3: *****")
print()
# Write a function to find the factorial of a number.
# The factorial of a number is the product of all the integers from 1 to that number. 
# For example, the factorial of 5 is 1*2*3*4*5 = 120
# def factorial(n):
#   c=1
#   for i in range(1,n+1):
#       c=i*c
#   return c
# u=int(input("Write a factorial number: ")) 
# product=factorial(u)
# print("Your factorial number is",product) 
''' Task 4: LCM '''
print("***** Task 3: *****")
print()
# Create a function to find the LCM of two numbers.