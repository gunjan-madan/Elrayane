# Have you wondered what would happen if you had an infinite loop? 
# It is important to break away from an infinite loop else, the computer keep processing without any end
# Let us take a look at some programs that help break from a loop

'''Task 1: Whats the price '''
print("**** Task 1: ****")
print()
# Write a program that takes the price of goods sold as inputs from the user.
# To stop entering or when the user is done, he or she news to press 0.
# Once the user is done,the program must print
# - Total cost  of the goods 
# - Total number of goods.
# c=0
# t=0
# p=3
# while p>0:
#   p=float(input("Enter a price for a product (Press '0' to quit): "))
#   if p!=0:
#     t=t+p
#     c=c+1
# print("The total cost of all your products is: ",t)  
# print("The total number of all your products is: ",c)





'''Task 2: Lemonade and Glasses '''
print("**** Task 2: ****")
print()
# Your friend Sam has a jar with 5 cups of fresh lemonade.  
# Jack has some glasses which hold 1.5 cups each of liquid.  
# How many glasses of lemonade can Jack serve?



'''Task 3: Population Calculator '''
print("**** Task 3: ****")
print()
# Sam is thrilled how he is able to solve problems
# He now wants to solve a population projection problem
# Can you solve it for him?
# He wants to know how long will it take to reach a certain target population (in years), given a 
# - starting population =10000000
# - birthrate=0.015
# - deathrate=0.023
# - Reduction can be taken as 0.1.
# Hint1: Target population can be calculated as population * reduction
# Hint2: Change in population can be calculated using the formula (current_pop * deathrate) - (current_pop * birthrate)

pop=10000000
trp= pop*0.1
cp=0
y=0
while pop>trp:
  cp=(pop*0.023)-(pop*0.015)
  pop=pop-cp
  y=y+1
print("Total number of years is:",y)

'''Great! You are exceptionally good at coming out with programming solutions. Way to go!!'''