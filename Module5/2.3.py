#Date, time, timezone

# Can we automatically calculate the  age of a person or find out if the current year is a leap year or not.
# Let's take a look.  

'''Task 1: All about dates'''
print("***** Task 1: *****")
print()
# Well!!Python has a module called datetime to work with dates and perform calculations.
# Uncomment the statements below and click Run

# import datetime
# x = datetime.datetime.now()
# print("The current date is: ", datetime.datetime.now())
# print("The date today is: ",x.day)
# print("The current month is: ", x.month)
# print("The current year is: ", x.year)

# # What do you think the program does? 
# # Here is a list of some of the datetime functions that have been used in the above program:
# # datetime.now()- Displays the current date 
# # day - Displays the current date from the date returned by the datetime.now() function
# # month - Displays the current month from the date returned by the datetime.now()
# # year - Displays the current year from the date returned by the datetime.now()

# '''Timezone '''
# #By default Datetime will display UTC (Universal Time)
# #To get time of a specific timezone, we need another module

# import datetime
# import pytz
# time_zone= pytz.timezone('US/Mountain')
# y= datetime.datetime.now(time_zone)
# print(y)

# List of all timezones
# for tz in pytz.all_timezones:
#   print(tz)


'''Task - Calculate age of the person'''
# Write a program that calculates the age of a person using the list of functions given in the table. 
# age based on years:present - birth age based on months: present month
# import datetime
# year=int(input("What was the year you were born in: "))
# month=int(input("What was the month you were born in: "))
# present_time=datetime.datetime.now()
# present_year=datetime.datetime.now().year
# present_month=datetime.datetime.now().month
# if present_month>month:
#   calc_year=present_year-year
#   calc_month=present_month-month

# else:
#   calc_year=present_year-year-1
#   calc_month=12-(month-present_month)

# print("Your age is:",calc_year,"years old",calc_month,"months  see***MAGIC***")

'''Task 2: Is it a leap year or not'''
print("***** Task 2: *****")
print()
# Write a program to find if the current year is a leap year or not
# Hint: Any year that is divisible by 4  or 400 is a leap year
# import datetime
# present_year=datetime.datetime(1524,4,5).year
# if present_year%400==0:
#   print("LET'S GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO IT'S IS A LEAP YEAR")
# elif  present_year%100!=0 and present_year%4==0:
#   print("LET'S GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoooooooooo IT'S IS A LEAP YEAR")
# else:
#   print("Pure sadness not a leap year :(")


'''Task 3: Number of Days'''
print("***** Task 3: *****")
print()
# Write a program to display the number of days in the current month
# Hint: Use the datetime.datetime.now().month function to get the month 
import datetime
present_month=datetime.datetime.now().month
if present_month in (1,3,5,7,8,10,12):
  print("YES SIR THIS MONTH HAS 31 DAYS, ENJOY IT WHILE IT LASTS.")
elif present_month in (4,6,9,11):
  print("ONLY 30 DAYS IN THESE MONTHS SADNESS.")  
else:
  print("IT'S FEBRUARY, THE DIVERGENT MONTH ONLY 29/28 DAYS.")  
'''Fantastic!! You are good at writing programs using the datetime module. Way to go!!'''