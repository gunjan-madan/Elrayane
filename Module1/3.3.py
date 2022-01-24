'''*****Task 1: BODMAS/PEMDAS - Setting the order******'''
print(" ")
print("*** Task 1:***")


# p=6 + 10 / 2                      #11
# q=(6 + 10) / 2                    #8
# r=2 + 3 * 5                       #17
# s=(2 + 3) * 5                     #25
# t=6 +(8 / 4) - 2 * 3              #2
# v=(6 + (8 / 4) - 2) * 3           #18
# print(p, q, r, s, t, v)
#print

'''*****Task 2: Display the Report Card******'''
print(" ")
print("*** Task 2:***")
# Once exams get over we all wait for our report cards.
# You too can create one in Python.
# To start you need to follow the below steps:
# Get the marks for the following subjects from the user : English, Science, Math, Computer Science and History
# Find the total marks and calculate the percentage scored
# Display both the total marks and the average achieved 
# [Hint: Total marks scored divided by the number of subjects gives you the average]
English=int(input("The English mark is: "))
Science=int(input("The Science mark is: "))
Math=int(input("The Math mark is: "))
Computer_Science=int(input("The Computer Science mark is: "))
History=int(input("The History mark is: "))
Total=(English+Science+Math+Computer_Science+History)
AV=(Total/5)
print("Total mark that's been achieved is: ",Total)
print("Avearage mark that's been achieved is: ",AV)