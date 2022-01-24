#Lets Learn using multiple conditions

age=14

if age>18:
  print("Play Pubg")
elif age>13:
  print("Play Bike City")
else:
  print("racing game")


"""-----Task 1:  What is your score? ---------"""
print(" ")
print("*** Task 1: ***")
# Write a program to get the marks for Mathematics from the user. 
# If the marks is less than 50 or equal to 50, print a message saying “you need to improve”.
# If the mark is between 50 and 80, print “ Let's work little more!”
# If the mark is more than 80, print “ You are doing good. Keep it up!”
# mark=int(input("write your math mark: "))
# if mark<=50:
#   print("you need to improve")
# elif mark<=80:
#   print("Let's work little more!")
# else:
#   print("You are doing good. Keep it up!")  





"""-----Task 2:  Which sides are equal? ---------"""
print(" ")
print("*** Task 2: ***")
#In this program we will take three sides of a triangle as input from user
#Compare the sides to check if they are equal
right=int(input("Write a number that present the right side of the triangle: "))
left=int(input("Write a number to present the left side of the triangle: "))
base=int(input("Write a number that presents the bese of the triangle: "))
if right==left==base:
  print("all the sides are equal")
elif right==left:
  print("the right and the left sides of the triangle are equal")
elif right==base:
  print("the right side and the base of the triangle are equal")
elif left==base:
  print("the left side and the base of the triangle are equal")
else:
  print("none of the sides are equal")        