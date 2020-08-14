"""
Author: Ohm Sabpisal
Credit: NONE
Class: CIS 122 Fall 2019
Date: November 9, 2019
Description: (LAB) This simple program will calculate your average, lowest, and highest grades.
"""

# Initialize Variables
input_grades = True
score_counter = 0
total_score = 0
low_score = -1
user_score_list = []


# Input Grades
while input_grades:
	user_score = input("Enter score: ")
	if len(user_score) == 0: # If empty then exit the loop by setting input_grades to False
		input_grades = False
	elif user_score != 0:
		score_counter += 1
		user_score = float(user_score) # Converts the String into a Float
		total_score += (user_score)
		user_score_list.append(user_score) # Add value the new user_score into the list. 

# Find the lowest and highest score from list.
low_score = min(user_score_list)
high_score = max(user_score_list)

if score_counter == 0:
	average_score = "No scores entered"
if score_counter != 0:
	average_score = "Average: " + str(total_score / score_counter)



print("*** Results ***")
print("Count: " + str(score_counter))
print(average_score)
print("Low score: " + str(low_score))
print("High score: " + str(high_score))
