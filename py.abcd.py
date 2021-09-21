      #Assignment 1
#Q1)Write a program to print the patters.
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3
# 1 2 
# 1
for i in range(0,5,1):
    for j in  range(0,5-i):
        print(j+1, end=" ")

    print()   




#Q-2) Write a program to print the pattern :   
# *
# **
# ***
# ****
# *****

for i in range(5):
    for j in range(i+1):
        print("*", end="")

    print()    