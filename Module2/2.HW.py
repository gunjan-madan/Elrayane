'''Task 1: Perimeter Calculator'''
print()
print("****Task 1: *****")
# Given below is a menu based Perimeter calculator.
# The calculator calculates the perimeter of:
# -  rectangle [Formula: 2*(length+width)]
# -  square [Formula: 4*length of side]
# -  circe[Formula: 2*(3.14*radius)]
# -  triangle [Formula: length + base + side]
# The menu has been created for you.
# Uncomment the statements and for each of the if statements write the relevant code.
print("***** Perimeter Calculator *****")
print("Select the shape for which the perimeter needs to be calculated")
print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Triangle")
choice=int(input("Enter your choice: "))
# rectangle
if choice==1:
  w=float(input("\nWrite the measurments for the rectangle's width: "))
  l=float(input("\nWrite the measurments for the rectangle's length: "))
  p=2*(l+w)
  print("\nThe perimeter of the rectangle you've given to us is:",p)
# square  
elif choice==2:
  l_s=float(input("\nWrite a measurment for the square's length of side: "))
  p=4*l_s
  print("\nThe perimeter of the square you've given us is:",p)
# circle   
elif choice==3:
  r=float(input("\nWrite a measurment for the radius of a circle: "))
  p=(3.14*r)*2
  print("\nThe perimeter of the circle you've given us is:",p)
# triangle
elif choice==4:
  l=float(input("\nWrite a triangle's length measurment: "))
  s=float(input("\nWrite a triangle's side measurment: "))
  b=float(input("\nWrite a triangle's base measurment: "))
  p=(l+s+b)
  print("\nThe perimeter of this triangle is:",p)
else:
  print("\nPlease write one of the numbers that we have provided you with")  