# 1. Python List Transformation

# Objective: The aim of this assignment is to practice advanced list operations and transformations.

# Problem Statement: You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.


# Task 1: Given the list of grades:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order and display the sorted list.
grades.sort(reverse = True)
print(grades)


# Task 2: Calculate the average grade from the list above and display it (reminder: The average is calculated by dividing the sum of all grades by the length of the grades list).
average_grades = sum(grades) / len(grades)
print(average_grades)




# 2. Advanced Slicing Techniques

# Objective: The aim of this assignment is to master the art of slicing in Python lists.

# Problem Statement: You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures:
#               0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23   24   25   26   27   28   29
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperatures.sort #They are already sorted but i added this just incase they werent already. 

# Extract the temperatures for the second week (7 days) of the month. Expected Outcome:
# 83, 85, 86, 87, 88, 89, 90,
second_week = temperatures[7:14]
print(second_week)

# Task 2: Extract all the temperatures above 100 (reminder: when slicing to the end of a list you don't need a stop index).
temp_over_100 = temperatures[23:]
print(temp_over_100)

# Task 3: extract temperatures from the 5th to the 10th.
specific_days = temperatures[4:10]
print(specific_days)