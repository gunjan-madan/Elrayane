# Sam is slowly realising that he can solve Maths problems with while loops.
# So he wants you to help him with them.
# Are you ready to help him?
''' Task 1: Multiplication Table Generator '''
print("**** Task 1: ****")
print()
# Sam wants you to write a program that can generate a multiplication table for any number that is specified
# Remember to get the number for which the multiplication table needs to be generated from the user
# print("***Multiplication table that stops at 1000")
# c=int(input("Write a number, and will make for you it's multiplication table: "))
# s= 1
# while s<=10000:
#   r= s*c
#   print(c," x ",s," = ",r)
#   s= s+1


''' Task 2: Whats the Average '''
print("**** Task 2: ****")
print()
# Help Sam write a program to calculate the average of five numbers.
# You need to get the numbers as an input from the users. You need to place the input statement within a while loop so that it gets executed n number of times and waits for the user input after every iteration.
# The first few lines of the program have been done for you. Uncomment them, complete the program and execute it to see if you get the result.

tot=0
counter = 1  	    
while counter <=5:
  c=int(input("write a number of your choice: "))
  tot= tot+c
  counter= counter+1
a= tot/5
print("YoUr AvErGe Is:",a)


''' Task 3: Skip Counting '''
print("**** Task 3: ****")
print()
# Sam is having fun with trying out math concepts in Python.
# He now wants to create a program which accepts a starting number and an ending number, which he calls the number limit. 
# Once that is done, he wants the program to print every third number that is within the number limit.
# Are you ready to take this challenge up?
u=int(input("Write a starting number: "))
uu=int(input("Write an ending number: "))
while u<=uu:
  print(u)
  u= u+3