# 1. The Range Riddle
# Objective: The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.

# Task 1: Every Other Day 
# Write a program that prints each day of the week, but only if that day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i, day in enumerate(days_of_week): #This for loops allowes me to break the list into pair the day to a number.
    if i % 2 == 0: #The i pulls the iterative number and and devides it by 2 checking to see if there is any rammainder. If there is no remainder it is on an even number.
        print(day) # Prints the ones that a found true for i. 


# 3. Loop Condition Logic
# Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.


# Task 2: Conditional Exit 
# Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)
fingers = 0 # Starts at 0
print("Dont make me count to 5!") #Fair warning
while fingers < 5: 
    fingers += 1
    if fingers == 1:
        print(f"Ok thats it! {fingers} ")
    elif fingers == 2:
        print(f"You better stop! {fingers} ")
    elif fingers == 3:
        print(f"I wont say it again! {fingers} ")
    elif fingers == 4:
        print(f"You've really done now! {fingers} ")
    else:
        print(f"Final warning! {fingers}")
    
# 4. Python's Random Game Night
# Objective: The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.
#
# Task 1: Random Choice Game Create a game where a player has a list of items. 
# They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. 
# Provide feedback on whether they guessed correctly or not keep them playing unitl they guess correctly. 

import random
total_fingers = [1, 2, 3, 4, 5 ]
while True:
    user_choice = int(input("How many fingers am I holding behind my back up on one hand?: ")) #User input 1-5.
    computer_choice = random.choice(total_fingers) #Computer randomly generates a number.
    #print(computer_choice) (used for testing to verify the number)
    if user_choice == computer_choice: #if the inputs == each other print congrats and break the loop. 
        print("[]~(￣▽￣)~* OHHHHH YA you got it! (Radish Spririt dances in the background!) []~(￣▽￣)~*")
        break
    else:
        print("Thats not correct, please try again.") # else try again.

    
    

    

