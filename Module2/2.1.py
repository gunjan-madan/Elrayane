#Conditions along with Arithmetic operations


'''-----Task 1: Speed, Distance, Time Calculator------'''
print("****Task 1: ****")
print()
# Write a program which calculates the speed or distance or time depending on the inputs provided by the user
# Ask the user what they want to calculate and depending on the response, ask for the required inputs, 
# For example if the user says the speed needs to be calculated, take the distance and time as the input from the user


# w=input("Select what you want to calculate:\n1.Speed    \n2.Distance\n3.Time\n")
# if w=="1":
#   d=int(input("Write the distance: "))
#   t=int(input("Write the time: ")) 
#   s=d/t
#   print("The speed is equal to: ",s)
# elif w=="2":
#   s=int(input("Write the speed: ")) 
#   t=int(input("Write the time: "))
#   d=s*t
#   print("The distance is equal to: ",d)
# elif w=="3":
#   s=int(input("Write the speed: ")) 
#   d=int(input("Write the distance: "))
#   t=d/s
#   print("The time is equal to: ",t)
# else:
#   print("PLEASE write a valid input")  

'''-----Task 2: Total Score------'''
print("****Task 2: ****")
print()
# Write a program that takes the Maths theory and Maths lab score. 
# Each of the score cannot be more than 50 
# Calculate the total score and print the result
i=int(input("Write the Math theory's score: "))
d=int(input("Write the Math lab score: "))
if i>=50 or d>=50:
  print("You are lying about your mark")
else:
  T=i+d
  print("Good job your total score is: ",T)