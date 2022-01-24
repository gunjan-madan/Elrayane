# Mr.Turtle is impressed with your skills of creating the different shapes and now, wants to fill the shapes with colours.
# Are you excited?

''' Task 1: Let's fill the hollow circle '''
print("***** Task 1: *****")
print()
# Uncomment the statements below and click Run. Observe the output

# import turtle
# turtle.shape("turtle")
# turtle.pensize(4)
# turtle.penup()
# turtle.goto(0,-70)
# turtle.pendown()
# turtle.fillcolor("yellow")
# turtle.begin_fill()
# r = 100
# turtle.circle(r)
# turtle.end_fill()
# # eye number 1
# turtle.penup()
# turtle.goto(-50,60)
# turtle.pendown()
# turtle.fillcolor("black")
# turtle.begin_fill()
# turtle.circle(15)
# turtle.end_fill()
# # eye number 2
# turtle.penup()
# turtle.goto(50,60)
# turtle.pendown()
# turtle.fillcolor("black")
# turtle.begin_fill()
# turtle.circle(15)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(-70,10)
# turtle.pendown()
# turtle.setheading(-60)
# turtle.circle(80,120)
# turtle.hideturtle()

# In the program we have used the fillcolour ( ) function, along with the name of the colour.
# Next we call the begin_fill ( ) function and start drawing. 
# Then we call the end_fill ( ) function to fill the shape with the specified colour.

''' Task 2: Solid squares and rectangles '''
print("***** Task 2: *****")
print()
# Write a program to create a square and a rectangle seperately. Fill it with the colour of your choice.

# import turtle

# # Square
# bob=turtle.Turtle()
# bob.shape("turtle")
# bob.color("black","#FFA20D")
# bob.pensize(4)
# bob.pendown()
# bob.begin_fill()
# for b in range(4):
#   bob.forward(90)
#   bob.right(90)
# bob.end_fill() 
# # Rectangle
# bob.penup()
# bob.forward(150)
# bob.pendown()
# bob.begin_fill()
# bob.forward(90)
# bob.right(90)
# bob.forward(150)
# bob.right(90)
# bob.forward(90)
# bob.right(90)
# bob.forward(150)
# bob.end_fill()
# for n in range(999999999999999999999):
#   bob.fillcolor("#FF1200")
#   bob.fillcolor("#7DFF0F")
#   bob.fillcolor("Navy")
#   bob.fillcolor("cyan")
#   bob.fillcolor("#FF008C")
#   bob.fillcolor("#FFD90F")
#   bob.fillcolor("#FE7B00")
#   bob.fillcolor("#EA65BE")
#   bob.fillcolor("#FFB657")
#   bob.fillcolor("#00FF59")
#   bob.fillcolor("#2AFE33")




''' Task 3: Building a House '''
print("***** Task 3: *****")
print()
# Mr. Turtle is ready with his next challenge where he wants you to create a house using only a square and a triangle.
# Are you ready to give it a try?
# Hint: Ensure that the base of the triangle and the side facing the top of the square are the same

import turtle
turtle.clearscreen()
turtle.shape("turtle")
turtle.color("black","#F02B10")
turtle.bgcolor("white")
turtle.pensize(5)
turtle.penup()
turtle.goto(150,100)
turtle.speed(100)
def house():
  turtle.pendown()
  turtle.begin_fill()
  for i in range(3):
    turtle.forward(90)
    turtle.left(120)
  turtle.end_fill()
  turtle.begin_fill()
  turtle.left(180)
  turtle.forward(220)
  turtle.right(120)
  turtle.forward(90)
  turtle.right(60)
  turtle.forward(220)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(240,100)
  turtle.pendown()
  turtle.fillcolor("#FA5043")
  turtle.begin_fill()
  turtle.right(90)
  turtle.forward(185)
  turtle.right(90)
  turtle.forward(310)
  turtle.right(90)
  turtle.forward(185)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(151,100)
  turtle.pendown()
  turtle.fillcolor("#43FAEB")
  turtle.left(180)
  turtle.forward(185)
  turtle.penup()
  turtle.goto(130,50)
  turtle.pendown()
  turtle.right(90)
  turtle.begin_fill()
  for s in range(4):  
    turtle.forward(60)
    turtle.left(90)
  turtle.end_fill()  
  turtle.penup()
  turtle.goto(99,50)
  turtle.pendown()
  turtle.left(90) 
  turtle.forward(60)
  turtle.right(270) 
  turtle.penup()
  turtle.goto(69,21)
  turtle.pendown()
  turtle.forward(60)
  turtle.penup()
  turtle.goto(21,50)
  turtle.pendown()
  turtle.right(90)
  turtle.begin_fill()
  for ss in range(4):
    turtle.forward(60)
    turtle.right(90)
  turtle.end_fill()  
  turtle.penup()
  turtle.goto(-10,50)
  turtle.pendown()
  turtle.forward(60)
  turtle.left(90)
  turtle.penup()
  turtle.goto(-40,21)
  turtle.pendown()
  turtle.forward(60)
  turtle.left(90)
  # The door
  turtle.penup()
  turtle.goto(175,-85)
  turtle.pendown()
  turtle.fillcolor("#8C5303")
  turtle.begin_fill()
  turtle.forward(80)
  turtle.right(90)
  turtle.forward(40)
  turtle.setheading(90)
  turtle.circle()
  turtle.left(90)
  turtle.forward(40)
  turtle.right(90)
  turtle.forward(80)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(201,-52)
  turtle.pendown()
  turtle.fillcolor("yellow")
  turtle.begin_fill()
  turtle.circle(5)
  turtle.end_fill()
  turtle.hideturtle()

house()  


''' Task 4: Twinkling Stars '''
print("***** Task 4: *****")
print()
# Mr.Turtle has a bonus challenge for you and he wants you  to create a star using two triangles. To begin with he wants you to call this turtle a star. You can do that by using the Turtle() function as follows:
#star = turtle.Turtle()
# The Turtle() function creates a new instance of turtle. Mr.Turtle has written the first few lines of code.  
# Uncomment the statements and complete the code.
import turtle
turtle.clearscreen()
star = turtle.Turtle()
star.shape("turtle")
star.color("#FFC030","#FFC030")
star.pensize(4)
star.begin_fill()
for i in range(3):
  star.forward(90)
  star.left(120)
star.end_fill()  
star.penup()
star.goto(0,60)
star.right(60)
star.pendown()
star.begin_fill()
for c in range(3):
  star.forward(90)
  star.left(120)
star.end_fill() 
# perfect star
t=turtle.Turtle()
t.color("limegreen")
t.penup()
t.goto(-90,-50)
t.pendown()
for i in range(5):
  t.forward(150)
  t.right(144)

''' Task 5: Olympic Ring '''
print("***** Task 5: *****")
print()
# Writeforward(100) a program to create the olympic ring and impress Mr.Turtle with your skills

import turtle
turtle.clearscreen()
bob=turtle.Turtle()
bob.shape("turtle")
bob.color("#2D8FE1")
bob.pensize(10)
bob.speed(100)
bob.penup()
bob.goto(-170,40)
bob.pendown()
bob.circle(80)
bob.penup()
bob.goto(-75,-30)
bob.pendown()
bob.color("#F1C033")
bob.circle(80)
bob.penup()
bob.goto(20,40)
bob.pendown()
bob.color("black")
bob.circle(80)
bob.penup()
bob.goto(115,-30)
bob.pendown()
bob.color("#11B92D")
bob.circle(80)
bob.penup()
bob.goto(205,40)
bob.pendown()
bob.color("#E13E7A")
bob.circle(80)
bob.hideturtle()



''' Wow!! You came up with some really creative graphics/drawings. Way to go champ!! '''

turtle.done()