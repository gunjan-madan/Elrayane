# You have just learnt how to use built-in functions with numbers.
# Let’s take a look at how to use built-in functions on strings.

'''Task 1: upper and lower '''
print("***** Task 1: ***** ")
print()

# Let us use the lower() function.
txt="Hello. New House Owner.!"
# txt1=txt.lower()
# print(txt1)

# Let us use the upper() function.
# txt2=txt1.upper()
# print(txt2)

# Here we will use the replace() function. Uncomment the statement below and execute it.
txt3 = txt.replace("Hello","21")
print(txt3)

#The format of replace function is as follows:
#  string.replace(oldvalue, newvalue, count). Here 
#   - oldvalue is the string to search for
#   - newvalue is the string replace the old value with
#   - count is optional and is a number specifying how many occurrences of the old value you want to replace. Default is all occurrences

# Here to split, the separator is the", ". So let us use the split() function. Uncomment the statement below and execute it.
x = txt3.split(".")
print(x)

'''Task 2: What's the code? '''
print("***** Task 2: ***** ")
print()
# Given below is the code to enter a new house.
# Coded password is: "Hello My Master, I am your New House."
# Write a program to do the following:
#  - Convert it into upper case
#  - Replace word “House” with “AppleTree”
#  - Split the message, where in the separator is the", ".
# password="Hello My Master, I am your New House."
# pas=password.upper()
# pas2=pas.replace("Hello","Apple Tree")
# pas3=pas2.split(", ")
# printpas3)


'''More functions '''
name = "gunjan"
value ="12"
space= " "
print(name.isupper())
print(name.islower())
print(len(name))
print(name.isnumeric())
print(value.isnumeric())
print(space.isspace())

# Here is a list of the functions we used in the program
# string.isupper() - The isupper() function returns True if all the characters are in upper case, otherwise False.
# string.islower() - The islower() function returns True if all the characters are in lower case, otherwise False.
# len(string) - The len() function returns the number of characters in the string.
# string.isspace() - The isspace() function returns True if all the characters in a string are whitespaces, otherwise False.
# string.isnumeric() -The isnumeric() function returns True if all the characters in the text are numeric

'''Task 3: Secret Code '''
print("***** Task 3: ***** ")
print()
# Studmonkey has set some instructions for anyone entering the kitchen: 
# - User to provide their first name and surname/last name in upper case:
# - User to provide their first name and surname/last name in upper case
# - User to provide their age. The age should be a double digit like 13, 14, 22 etc.
# - User to provide a secret code word which they will use each time they enter the kitchen. The code word should not have any space and should be in lower case

# nme=input("Provide us with your first name in upper case: ")
# nme1=input("Provide us with your last name in upper case: ")

# if nme.isupper() and nme1.isupper():
#   age=input("Provide us with your age: ")
#   if len(age)==2:
#     code=input("Write a secret code which you will be using every time you enter MY   KITCHEN(make it in lower case, and without spaces): ")
    
#     if code.islower() and code.isspace()==False:
#       print("YOU HAVE FINALLY SUCCEDED IN WHAT NO BODY HAS EVER SUCCEDED TO DO, YOU HAVE FINALLY ENTERED MY CASTLE/KITCHEN, NOW COOK SOMETHING FOR ME.")
#     else:
#       print("ARE YOU 5, READ THE INSTRUCTION THAT I'VE GIVEN TO YOU IN THE CODE")
#   else:
#     print("ARE YOU 5, READ THE INSTRUCTION THAT I'VE GIVEN TO YOU IN THE CODE")
# else: 
#   print("WRITE YOUR NAME IN UPPER CASE AS I HAVE OVIOUSLY WRITTEN TO YOU") 


'''Task 4: Ready for an adventure '''
print("***** Task 4: ***** ")
print()
# You are in charge of  taking in applications for the Summer Adventure workshop. You need to ensure that when applying students:
# - Enter their full name in upper case
# - Enter a valid age
# - Provide an email address and not leave it empty

count=0
while True:
  nme=input("Write your name in upper case please: ")
  age=input("Write your age: ")
  email=input("Write your parents email I know you memorize it: ")
  if nme.isupper() and age.isnumeric() and len(email)>0:
    if count==0:
      print("WOW, I am impresed you haven't made any mistakes. I'm proud of you")
    else: 
      print("YOU ESCAPED THE MISTAKES ABYSS")
      print("You have succeded in writing my orders right with a total mistakes of ",count)
    break
  else:
    count+=1
    print("YOU HAVE FALLEN IN THE MISTAKES ABYSS NOW RUN THE PROGRAMM AGAIN   AND SUFFER/READ THE INSTRUCTIONS") 