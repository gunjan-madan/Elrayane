# In the previous lesson, you used if-elif-else statements to create a menu based program.
# Now let us take a look at using nested if-elif statements in creating menu based programs.
'''Task 1: Nested If-else'''
print()
print("*** Task 1: ***")
print()
#Make a variable like winning_number and assign any number to it between 1 and 20.
#Ask user to guess a number between 1 and 20. (Take input)
#if user guessed correctly, print "YOU WIN"
#if user didn't guessed correctly then:
  #if user guessed lower than actual number, then print "TOO LOW"
   #if user guessed higher than actual number, then print "TOO HIGH"

# guess=int(input("Write any number you think of between 1 and 20: "))
# winning_number=17
# if guess==winning_number:
#   print("YOU WON")
# else:
#   if guess>winning_number:
#     print("your guess is too high")
#   else:
#     print("your guess is too low")  



'''Task 2: Nested If-else'''
print()
print("*** Task 2: ***")
print()
#This is a program to tell User the shipping cost based on the country and the weight.
#Write a Program that takes two inputs: country_code(AU/US) and weight of the product.
#Use the following conditions to find the shipping cost
#country          Product Size               Shippping cost
#US               less than 1kg               $5
#US               between 1 and 2kg           $10
#US               greater than 2kg            $20
#AU               less than 1kg               $10
#AU               between 1 and 2kg           $15
#AU               greater than 2kg            $25

# print("This Program will caluculate Shipping Cost")
print("    Sir/Madam, this programm will calculate your shipping cost in AU or US")
cou=input("\ncould you please provide us the country you live in AU or US: ")
if cou.upper()=="US":
  u=float(input("\nhow much KG are you trying to ship: "))
  if u<=1:
    print("your shipping cost is equal to $5")
  elif u<=2:
    print("your shipping cost is equal to $10")
  elif u>2 and u<5:
    print("your shipping cost is equal to $20")
  else:
    print("your package is too heavy to be shiped")  
elif cou.upper()=='AU':
  u=float(input("\nhow much KG are you trying to ship: "))
  if u<=1:
    print("your shipping cost is equal to $10")
  elif u<=2:
    print("your shipping cost is equal to $15")
  elif u>2 and u<5:
    print("your shipping cost is equal to $25") 
  else:
    print("your package is too heavy to be shiped")    
else:
  print("\nsorry Sir/Madam, but our service is only in AU/US")      