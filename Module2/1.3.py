# You used the if elif statement to handle multiple conditions.
# What if you have 10 conditions to evaluate? Will you write 10 if..elif statements? 
# Is it possible to check for more than one condition in a single if statement or elif statement? 
# Let's check it out  

# grade= "8th"
# gender= "Male"

# if (grade=="8th" or grade=="9th") and gender=="Male":
#   print()
  



"""-----------Task 1:  All in One ---------------"""
print(" ")
print("*** Task 1: ***")
# Do you know what are isosceles and scalene triangles? 
# Write a program to check if a triangle is equilateral, scalene or isosceles.
# Left_side_of_the_triangle=float(input("enter the measurements for the left side of the triangle: "))
# Right_side_of_the_triangle=float(input("enter the measurements for the right side of the triangle: "))
# The_base_of_the_triangle=float(input("enter the measurements for the base of the triangle: "))
# if Left_side_of_the_triangle==Right_side_of_the_triangle==The_base_of_the_triangle:
#   print("This triangle is equilateral")

# elif Right_side_of_the_triangle==Left_side_of_the_triangle or Left_side_of_the_triangle==The_base_of_the_triangle or The_base_of_the_triangle==Right_side_of_the_triangle or The_base_of_the_triangle==Left_side_of_the_triangle:
#   print("This triangle is isosceles")

# else:
#   print("This trinagle is scalene")




"""-----------Task 1.2:  All in One ---------------"""
print(" ")
print("*** Task 1.2: ***")
#The program takes a number as an input
#Program shall check if the number is divisible by both 3 and 4
# Write=float(input("Write a number and see if it's divisible by 3 and 4: "))
# if Write%3==0 and Write%4==0:
#   print("The number is divible by 3 and 4")
# else:
#     print("The number is not divisble by 3 and 4")
  




"""---------Task 2:   Its raining Discount -------------"""
print(" ")
print("*** Task 2: ***")
# Your store is giving a discount on the total purchase amount based on customer membership. 
# Write a program that calculates the discounted amount based on the below mentioned conditions:
# If membership is silver, 5% discount
# If membership is silver+ or gold, discount is 10%
# If membership is gold+ or diamond, discount is 15%
# if membership is platinum membership discount is 20%
# T_P=float(input("Write a total cost of your purchases: "))
# MM=input("Write is your membership: ")

# # If membership is silver, 5% discount
# if MM=="silver":
#   D_P=T_P-(T_P*0.05)

# # If membership is silver+ or gold, discount is 10%
# elif MM=="silver+"or MM=="gold":
#   D_P=T_P-(T_P*0.10)

# # If membership is gold+ or diamond, discount is 15%
# elif MM=="gold+"or MM=="diamond":
#   D_P=T_P-(T_P*0.15)

# # if membership is platinum membership discount is 20%
# elif MM=="platinum":
#   D_P=T_P-(T_P*0.20)
# else:
#   D_P=T_P  
# print("Your total cost is: ",D_P)





"""---------Task 3:   Theme Rides -------------"""
print(" ")
print("*** Task 3: ***")
# You are managing the ticket counter at Imaginika Theme Park. Based on the age of the entrant, you issue tickets for the rides"
# Age between 5 and 7 :Toon Tango, Net Walk
# Age between 8 and 12: Wonder Splash, Termite Coaster Train
# Age greater 13: Hang Glider, Wave Rider
# If the age criteria does not match they can go for the nature walks
# Write a program that grants access to the rides based on the age conditions.
age=int(input("Write your age: "))
# Age between 5 and 7 :Toon Tango, Net Walk
if age>=5 and age<=7:
  print("You are allowed to be in the Toon Tango, Net Walk")
  # Age between 8 and 12: Wonder Splash, Termite Coaster Train
elif age>=8 and age<=12:
  print("You are allowed to be in the Wonder Splash, Termite Coaster Train") 
# Age greater 13: Hang Glider, Wave Rider
elif age>=13:
  print("You are allowed to be in the Hang Glider, Wave Rider")
# If the age criteria does not match they can go for the nature walks
else:
  print("You can go for the nature walks")