'''*****Task 1: Arithmatic Calculator*****'''
print(" ")
print("*** Task 1:***")
# Extend the additive calculator to a basic Math calculator
# Write a program that does the following:
  # 1. Accept two integers from the user 
  # 2. Display separately on three lines: 
  # 3. The sum of the two numbers. 
  # 4. The difference of the two numbers (first - second). 
  # 5. The third line contains the product of the two numbers
# Num_1=int(input("write the firt number: "))
# Num_2=int(input("write a second number: "))
# add=Num_1+Num_2
# difference=Num_1-Num_2
# product=Num_1*Num_2

# print("The sum of two numbers is: ",add)
# print("The difference of two numbers is : ", difference)
# print("The product of the two numbers is: ",product)
'''******Task 2:  Grocery Checkout : Lets get calculating******'''
print(" ")
print("*** Task 2 :***")
# Ready for a role play.
# You work at the "Freshmart Grocery Shop" as an accountant
# Your manager has given you the following rate card:
# 1 kg of cauliflower - Rs. 30
# 1 kg of potato - Rs. 15
# 1 kg of Onion - Rs. 20
# 1 kg of Beans - Rs 25
# This week happens to be the discount week for customers. 
# You need to give the customer a discount of 10% on the total purchase.
# You have a customer who has bought:
# 2 kg of potato
# 1 kg of onion
# 1 kg of beans 
# 2 kg of cauliflower
# Write a Python program to calculate the amount the customer needs to pay.
add=2*15+20+1*25+2*30
discount_amount=add*0.1
Total_cost=add-discount_amount
print("The total price that the costumer has to pay is: ",Total_cost)