#Real Life Problems

'''Task 1:  Delivery Charges'''
print("***** Task 1: *****")
print()
# Create a program that takes the following input from the user:
# - The total number of sand sack and cement sack 
# -  Weight of each sack [Hint: use for loop to get the weight]
# - Use a variable to which the weight of the sack gets added as entered [Hint: calculate this within the for loop]
# - Calculates the total cost if each sack cost INR 300 [ outside the for loop]
# So let's get started

u=int(input("How much sand/cement sacks do you have: "))
w=0
for c in range(1,u+1):
  print("Weight of sack number ", c)
  e=int(input("Write the weight: "))
  w=w+e
tc=w*300
print("\nYour total cost is:",tc,"$")
print("The total weight of your items is:",w)


'''Task 2:   Lets go Outdoors'''
print("***** Task 2: *****")
print()
#Write a program that takes care of outdoor field trips for kids.
# The program needs to:
# - Take the total number of kids (Number cannot be more than 8)
# - Get the name, and address for each kid
# The program must display the total cost for the field trip where
# - Cost for food for each kid is INR 500
# - Cost for travel for each kid is INR 1000

# u=int(input("What is the total number of kids do you have?: "))
# if u>8:
#   print("We can not allow you in the park, becaue the max number of kids is 8")
# else:
#   for c in range(1,u+1):  
#     e=input("What is your kid's name: ")
#     b=input("What is your kid's address: ")
#   v=500*u
#   print("\nThe total cost of food for all the kids is:",v,"INR")
#   n=1000*u
#   print("\nThe total cost for traveling for all the kids is:",n,"INR") 
#   tc=n+v
#   print("\nThe total cost for the entire feild trip is:",tc,"INR")