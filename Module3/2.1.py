#while loop along with if conditions

# Have you been to a game arcade? 
# Which of the games are your favourite? 
# Are you ready to design one?
''' Task 1: Number Buzzer Game'''
print("**** Task 1: ****")
print()
# Write a “Guess the Number”  game, where a player has to guess a number between 10 and 20.  Let's assume that the number to guess is 15.
# Let's add some checks to the game, you have written:
# If the number is lesser than 10, you must give a warning message and ask them to guess again
# If the number is greater than 20, you must give a warning message for the same and ask them to guess again
# If the number is right, then you display a congratulatory message

# w=12
# i=int(input("take a guess of a number between 10 and 20: "))
# while i!=w:
#   if i<10 or i>20:
#     print("\mguess between 10 and 20")
#     i=int(input("take a guess of a number between 10 and 20: "))
#   else:
#     print("\nguess again")
#     i=int(input("take a guess of a number between 10 and 20: "))
# if i==w:
#   print("\nCongratulation you won the lotery")

''' Task 2: Break the loop'''
print("**** Task 2: ****")
print()
# Now let's bring in a twist in the program you wrote in Task 1. # You need to modify the program, in a way that it allows only 3 chances to guess the number.
# w=12
# x=3
# while x>0:
#   i=int(input("take a guess of a number between 10 and 20: "))
#   if i!=w:
#     if x>1:
#       print("\ntry again")
#     else:
#       print("\nSorry, you lost! hhhhhhhhhh")
#   else:
#     print("\nYou won the lotery")
#     break
#   x=x-1

''' Task 3: To quit or not to quit'''
print("**** Task 3: ****")
print()
# Write a program that takes numbers between 1 and 100 from the user.
# To quit entering numbers the user needs to press 0. 
# The program should then display the sum and the product of the numbers.
print("Choose a number between 1 and 100 (if you want to quit choosing     type 0) at the end we will tell you the product and the sum of the  numbers you chose")
x=0
u=8
c=1
while u!=0:
  u=int(input("\nChoose a number: "))
  if u!=0:
    x=x+u
    c=c*u
print("Your total addition is:",x)  
print("Your total multiplictaion is:",c)   

