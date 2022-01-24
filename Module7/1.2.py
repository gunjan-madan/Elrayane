# Mr. turtle found you to be good working with the turtle module.
# He has been given a set of challenges and needs your help.

'''Task 1: Perfect Square'''
print("****** Task 1: ******")
print()
# The first challenge that has been given to Mr. Mr.turtle is to make a square and he needs you to assist him.
# Here are some hints that will be of help:
# Draw a line by moving forward
# Turn 90 degrees left (anti-clockwise)
# Then draw a line by moving forward.
# Turn 90 degrees left (anti-clockwise)
# Repeat the first four lines of the algorithm again to complete a square.
# To start, he has already written the first few lines of code. Uncomment the statements below and complete the rest of the code.
# import turtle 
# turtle.shape("turtle")
# turtle.color("aquamarine")
# turtle.bgcolor("black")
# def square(size):
#  turtle.pensize(4)
#  turtle.pendown()
#  turtle.forward(size) 
#  turtle.left(90) 
#  turtle.forward(size) 
#  turtle.left(90) 
#  turtle.forward(size) 
#  turtle.left(90) 
#  turtle.forward(size) 
#  turtle.left(90)

# for i in range(100):
#   square(100)
#   turtle.speed(5)
#   turtle.left(10)
''' Task 2: Let's define the rectangle '''
print("***** Task 2: *****")
print()
# Mr. Turtle’s next challenge is to draw a rectangle of length 100 pixels and width 50 pixels.
# He realizes that drawing a rectangle is similar to drawing a square. So he started writing the first few lines of code and wants you to help him complete the code.
# Uncomment the statements given, complete the code to create a rectangle and then click Run.
# import turtle
# turtle.clearscreen()
# turtle.shape("turtle")
# turtle.color("gold")
# turtle.bgcolor("black")
# turtle.pensize(4)
# turtle.pendown()
# def rectangle(size):
#     turtle.right(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(2*size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(2*size)
    


# for i in range(100):
#   turtle.speed(5)
#   rectangle(20) 
#   turtle.left(50)
#   if i%4==0:
#     turtle.color("red") 
#   elif i%4==3:
#     turtle.color("gold")
#   elif i%4==2:
#     turtle.color("cyan")
#   else:    
#     turtle.color("blue")

''' Task 3: Get the Circle Rolling '''
print("****** Task 3:  *****")
print()
# Mr.Turtle wants you to help him with a code, to make a circle.
# Unlike a square, where we had to give commands, the circle comes with an inbuilt command. For example: # circle (10)
# Here 10 is the radius.
# Now write a program to create a circle with radius 50. You also need to ensure that the: 
# - background colour is set to pink
# - turtle colour is set to black 
# - pen size is set to 5
# import turtle
# turtle.clearscreen()
# turtle.shape("turtle")
# turtle.color("black")
# turtle.bgcolor("pink")
# turtle.penup()
# turtle.pensize(5)
# turtle.pendown()
# turtle.circle(100)

''' Task 4: Angle or Triangle '''
print("***** Task 4: *****")
print()
# Mr. Turtle has reached the final stage of his challenge. He has been asked to draw a triangle. 
# He has attempted to write the code and wants you to check if it is working fine. Uncomment the statements and click Run to see if you are getting the triangle as the output.
# import turtle
# turtle.clearscreen()
# turtle.shape("turtle")
# turtle.color("black")
# turtle.bgcolor("cyan")
# turtle.pensize(3)
# turtle.penup()
# turtle.goto(-40,0)
# turtle.speed(5)
# turtle.pendown()
# for i in range(3):
#   turtle.forward(50)
#   turtle.left(120)

''' Task 5: Let’s get angle right '''
print("***** Task 5: *****")
print()
# Mr.Turtle wants you to take the challenge to the next level and draw a right angled triangle.
# Are you ready to take this challenge? Here are some hints to get you started:
# - First draw the alphabet L 
# - Then adjust the angle of the turtle to complete the triangle

# Letter L
import turtle
turtle.shape("turtle")
turtle.color("red")
turtle.bgcolor("black")
turtle.penup()
turtle.goto(0,0)
turtle.pensize(2)
turtle.speed(4)
turtle.pendown()
turtle.left(270)
turtle.forward(125)
turtle.right(270)
turtle.forward(83)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.right(57)
turtle.forward(150)
turtle.penup()
turtle.goto(0,0)
hyp= (125**2+83**2)**0.5
print(hyp)

'''Awesome work!! You really have a great knack of creating shapes.'''

turtle.done()