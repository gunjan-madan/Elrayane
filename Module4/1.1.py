
''' Task 1: Numerical Trial '''
print("**** Task 1: ****")
print()
# The first stage of the quest is a trial run. 
# The quest is asking you to analyze and observe the program output.
# Uncomment the statements below and click Run

# for i in range(15):
#  if (i % 2) == 0:
#    print(i,"is a even number")
#  else:
#    print(i,"is a odd number")

# The range() function, takes three arguments: range(start, stop, step)
#start and step and optional parameters.

# Uncomment the statement below and click Run:

# x=0
# #define a while loop
# while(x <4):
#  print(x)
#  x = x+1
#Define a for loop 
# for x in range(1,100,2):
#   print(x)


'''Task 2: Who is the odd one out'''
print("**** Task 2: ****")
print()
# Math πrate is ready to take the next small steps in the coding quest. 
# Write a program that prints the odd numbers that occur between the 10 and 20
# for c in range(10,21):
#   if (c%2)!=0:
#     print(c,"It's an odd number")


'''Task 3: Ready to Skip'''
print("**** Task 3: ****")
print()
# Do you remember the program that you wrote on skip counting? 
#Take three inputs from user: starting number, ending number and skip interval.
#Print respective numbers

# u=int(input("Write a number that you like the loop to start with: "))
# w=int(input("Write a number that you like the loop to end with: "))
# p=int(input("Write the skipping interval: "))
# for c in range(u,w+1,p):
#   print(c)

'''Task 4: Sum and Product'''
print("**** Task 4: ****")
print()
# Math πrate is very happy with your help. 
# You need to assist Math πrate in writing a program that takes a starting and ending number and then calculates the:
# Total sum of the numbers between the starting and ending number
# Product of the numbers between the starting and ending number

# print("*** Sum and Product of numbers of your choice ***")
# u=int(input("\nWrite a number that you like the loop to start with: "))
# w=int(input("Write a number that you like the loop to end with: "))
# y=0
# v=1
# for c in range(u,w+1):
#   y=y+c
#   v=v*c
# print("The sum of the numbers you chose is:",y)
# print("The product of the numbers you chose is:",v)

'''Task 5: Lets get Even'''
print("**** Task 5: ****")
print()
# Math πrate has been working with each of the coding quest tasks effortlessly with your help.
# He has been given another number based quest.
# He needs your help in writing a program that takes :
# A starting and and ending number as the input from the user
# For each number between that range:
# If the number is an even number, then the output must display the square of the number
# If the number is odd, then the output must display the cube of the number
# Are you ready to help him with the program? 

# If the number is odd, then the output must display the cube of the number
# If the number is an even number, then the output must display the square of the number
u=int(input("\nWrite a number that you like the loop to start with: "))
w=int(input("Write a number that you like the loop to end with: "))
for c in range(u,w+1):
  if c%2==0:
    print("The number",c," was even this is why we squared it",c**2)
  else:
    print("The number",c," was odd this is why we cubed it it",(c**3))
  