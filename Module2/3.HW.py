#Practice on Nested Else if

''' Task 1: Metric Convertor'''
print("**** Task 1:  ****")
print()
# Write a Metric Conversion program that converts from one metric to another metric.
# You can start with:
# 1. cm to inch (Hint: divide the cm value by 2.54)
# 2. inch to feet (Hint: divide the inch value by 12)
# 3. meter to kilometer (Hint: divide the meter value by 1000)
# You can add more to the list.
print("***Converting Metric***")
print("Select witch metric conversion you want the programm to do for you")
print("1.Cm to inchs")
print("2.Inchs to Feet")
print("3.Meter to Kilometer")
print("4.Kilometers to Miles")
m=input("Write the number of the metric conversion you want to do: ")
if m=='1':
  v=float(input("Write a vlaue for the metric you chose so we could convert it: "))
  c= v/2.54
  print(v,"Cm equals",c,"inch")
elif m=='2':
  v=float(input("Write a value for the metric you chose so we could convert it: "))
  c= v/12
  print(v,"inchs equals",c,"feet")
elif m=='3':
  v=float(input("Write a value for the metric you chose so we could convert it: "))
  c= v/1000
  print(v,"meter equals",c,"kilometers") 
elif m=='4':
  v=float(input("Write a value for the metric you chose so we could convert it: "))
  c= v*0.621371
  print(v,"Kilometers equals",c,"Miles")  
else:
  print("\nBRO, WRITE FROM THE OPTIONS THAT WE PROVIDED YOU WITH, IT'S NOT    THAT HARD. ") 