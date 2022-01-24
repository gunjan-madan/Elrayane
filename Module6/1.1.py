#Functions
#Functions are required to reuse the code

'''Task 1:  All about functions'''
print("****** Task 1: *****")
print()
# Uncomment  the statement below and click Run.

##Define a user-defined function
# def welcome():
#   print("Welcome to Python class!!")
# #Call the function
# welcome()
# welcome()
# welcome()
# welcome()
# welcome()

'''Task'''
# Write a function to print your name and grade
# def ng():
#   print("My name is Rayane and I am a grade 8 student")
# ng()
# ng()
''' Task 2: Redefine the function '''
print("****** Task 2: *****")
print()
#Sending the parameter to the function
# Uncomment  the statements and click Run

# def studentdetails(name):
#  print("Name is:", name)

 
# studname=input("Enter your name: ")
# studentdetails(studname)

# Modify the program to:
# - Take the grade and age as input from the user
# - Pass the grade and age as arguments to the function
# def ng(name,grade):
#   print("My name is",name,"and I am a",grade,"student.")
# n=input("What is your name: ") 
# g=input("What is your grade: ") 
# ng(n,g)
''' Task 3:  Point of return '''
print("****** Task 3: *****")
print()
# Uncomment the statement and click Run

# Define the function
# def addition(x,y):
#  z=x+y
#  return z
# #Call thenction

# num1=int(input("Enter the first number: ")) 
# num2=int(input("Enter the second number: "))
# result =addition(num1,num2)



# print("The sum is: ",result)

# The function : 
# - Takes two arguments as input
# - Adds them and returns the sum to the caller.
# A return statement helps the function pass data back to the caller.
# Modify the above function to take three arguments  and return their product
# def prod(x,y,n):
#  z=x*y*n
#  return z

# num1=int(input("Enter the first number: ")) 
# num2=int(input("Enter the second number: ")) 
# num3=int(input("Enter the third number: "))
# result =prod(num1,num2,num3)
# print("The solution is: ",result)



''' Task 4:  What goes around, comes around '''
print("****** Task 4: *****")
print()
# Create functions that take the radius as the argument and return the area and perimeter.
# Area function
# def ca(r):
#  c=r**2*3.14
#  return c
# # Area
# r=float(input("Write a measurment of a radius of your choice: "))
# result = ca(r)
# print("The area of the circle you gave us is:",result)
# # Perimeter function
# def cp(p):
#   b=r*2*3.14
#   return b
# # Perimeter
# resul=cp(r)
# print("The perimeter of the circle you gave us is:",resul) 

 

''' Task 5: Convert days to second '''
print("****** Task 5: *****")
print()
# Create a function that takes the number of days as an argument , converts it to seconds and returns the same.
def convert_seconds(days=1):
  convert_second=(days*24*60)*60
  return convert_second  
# Amout of days
days=int(input("Write an amount of days of your choice: "))
seconds=convert_seconds(days)
print("The ginormous amount of seconds based on the amount days you gave  us is:",seconds,"seconds")