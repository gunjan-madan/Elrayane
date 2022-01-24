#Chatbot
# Chatbot is a computer program that chats like a real person. For example Swelly is a Facebook Messenger chatbot.
# Take a look at this video, that shows what a conversational banking chatbot looks like:
# https://www.youtube.com/watch?v=SNQGypLBJys

'''Task 1: Product Inventory'''
print()
print("*** Task 1: ***")
print()
# You work in the inventory department of an Automobile company.
# You want to write a program that will help in:
# Taking the order quantity from the user and checking if there is enough stock of the item requested. [Hint: Set a value for the stock availability] 
# If there is then take the name, address and phone number from the user and let them know it will be sent to their address in 48 hrs.
# If not let the user know that, the item is not in stock and that they will receive an email once it is in stock


# q=int(input("How much stuff do you want: "))
# s=512
# if q<=s:
#   print("please provide the following statments for your shipment")
#   na=input("\nSir/mam, could you please write your name: ")
#   add=input("\nSir/mam, enter your address please: ")
#   ph=input("\nSir/mam, could you please enter your phone number: ")
#   print("\nSir/mam, your products would be shiped to you in 48h :)")
# else:
#   print("Sorry, your item is out of stock :(")
#   em=input("\nSir/mam, could you provide us with your email so we could notify you when your item is in stock: ")


'''------- Task 2: Flowers on a Click'''
print("*** Task 2: ****")
print()
# You have to write a program that asks a customer if they like bouquets 
# If yes, ask them to  select a flower bouquet of their choice. You can use the following to start with:
#  - Rose and Lily 
#  - Orchid and Tuberose
#  - Rose and Carnation 
#  - Carnation and Orchids 
# Once the customer specifies their choice, you need to:
#  - Tell them the cost
#  - Get their address
# And send a message that it will be delivered to that address and they can pay by card, cash or Google Pay
# If the customer does not like bouquets choice, tell them to visit the website
b=input("Do you like bouquets: ")
if b.lower()=='yes':
  t=input("please slect from the following types of flowers:\n1.Rose and Lily\n2.Orchid and Tuberose\n3.Rose and Carnation\n4.Carnation and Orchids\n")
  if t=='1':
    print("the cost of the flower you chose would be: $11")
    s=input("\nSir/madam, could you provide us with you address please: ") 
    print("thank you for writing your address :)")
  elif t=='2':
    print("the cost of the flower you chose would be: $13")
    s=input("\nSir/madam, could you provide us with you address please: ") 
    print("thank you for writing your address :)")
  elif t=='3':
    print("the cost of the flower you chose would be: $10")
    s=input("\nSir/madam, could you provide us with you address please: ")
    print("thank you for writing your address :)") 
  elif t=='4':
    print("the cost of the flower you chose would be: $9")
    s=input("\nSir/madam, could you provide us with you address please: ") 
    print("thank you for writing your address :)")
  else:
    print("Sir/mam, PLEASE write a valid input") 
else:
  print("OK, no flowers for you")  