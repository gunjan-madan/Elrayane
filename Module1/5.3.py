# You are a part of the sports committee in your apartment complex.
# The committee head wants your help in developing a rectangular piece of land into a playground
# Are you ready to use your Python programming skills in solving the issue.

"""-----------Task 1:  Getting the Sports Field Ready ---------------"""
print(" ")
print("*** Task 1: ***")
# The Committee Head wants to convert a rectangular piece of land which is 118.5 meters long and 67.5 meters wide into a sports field.
# You and your friends propose the idea of splitting the land into a football pitch and hockey pitch with the following measurements:
#  91.5m long and 55m wide [football pitch] 
#  27 m long and 20.5 m wide [hockey pitch]
# The Committee head loves the idea. He decides to:  
# - First fence the sports field first and then 
# - Put artificial grass/turf for the hockey pitch. 
# He asks you to give the measurement for both so that he can get the materials.
# You decide to write a Python program to calculate the measures.
# So why wait, get programming!!
# Hint: For fencing, you need to get the perimeter of the sports field which is rectangular ( formula: perimeter - 2 x(length + width))
# Hint: For the artificial turf/grass, you need to get the area of the rectangular hockey pitch (Area = length * width]
#Fence measurments for both hockey and football pitchs
F_P_P=(91.5+55)*2
H_P_P=(27+20.5)*2
print("The fence measurments for the footbal pitch would be: ",F_P_P)
print("The fence measurments for the hockey pitch would be: ",H_P_P)
#the artificial turf/grass for the hockey pitch
L=27
W=20.5
A_of_H_P=L*W
Total=A_of_H_P
print("The artificial turf/grass you'll need for the hockey pitch is: ",Total)
