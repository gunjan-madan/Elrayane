#keyword arguments
#We can specify argument name with the value so that caller does not have to remember order of parameters.

''' Task 1:  Order of parameters '''
print("***** Task 1: *****")
print()

# def studentDetails(name,ID, age, city, school):
#   print("Student's name is ", name)
#   print(name, "'s' ID is ", ID)
#   print(name, "'s' age is ",age)
#   print(name, "'s' resides in ", city)
#   print(name, "'s' studies in ", school )

# #Call the function
# studentDetails(name="Rayane",school="Vincent Massey",age=13,city="Calgary",ID=1100023588)

# #In the above way, we have to remember the order of parameters.

# studentDetails(name="Michael", age=12, city="NY", ID=1234, school="Sommerville")

''' Task 2:  Variable arguments '''
print("***** Task 2: *****")
print()
#We can also pass varying number of arguments to the function
# def myFun(*args): 
#     for arg in args: 
#         print (arg)

# print("Result of * args: ")
# myFun('Hello', 'Welcome', 'to', 'Python')

# ''' Task '''
# #Write a function that take **args (all integers and min 5 numbers) and find their average
# def findavearage(*nums):
#   total=0
#   for num in nums:
#     total=num+total
#   avearage=total/len(nums)
#   print(avearage,"is your avearage")

# findavearage(90,55,24,77,86,74)

# Write a function which will add "ed" at the end of every word. Send atleast 5 words
def edfunc(*words):
  for word in words:
      print(word  + "ed")

edfunc("Write","Type","eat","fast","vast","revolutioniz","represent","efficiency")    

''' Task 4:  Variable arguments with Keywords '''
print("***** Task 4: *****")
print()
#Can also pass varying number of arguments through keywords using double star
# def myFun2(**kwargs): 
#     for key, value in kwargs.items():
#         print ("% s == % s" %(key, value))


# print("\nResult of **kwargs")
# myFun2(first ='Coding', mid ='Is', last ='Interesting') 
# def studentDetails(**values):
#   name=""
#   for key, value in values.items():
#      if key== "name":
#        name= value
#      if key== "ID":
#         ID= value 

#   print("Student's name is ", name)
#   print(name, "'s' ID is ", ID)

# studentDetails(name="Rayane", ID="123")



''' Task '''
#Write a function that take **kwargs 
#Take five numbers input from user, send it to function using **kwargs with their keywords (First, Second, Third, Fourth, Fivth)
#Find the maximum and print the number along with the keyword
def kwarfunc(**kwargs):
  for key, kwarg in kwargs.items():
    print(key,kwarg)
kwarfunc(First=1,Second=2,Third=,Fourth=7,Fifth=9)    
