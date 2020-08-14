"""
Author: Ohm Sabpisal
Credit: NONE
Class: CIS 122 Fall 2019
Date: November 15, 2019
Description: (ASSIGNMENT) This program will read line of text file and do certain logical manipulations
Part I, II, III
"""
# Import Libraries
from cis122_assign06_shared import pad_left, pad_right
import os

# Initialize Variables
# filename = 'random_numbers.txt' # Set Filename equal to random_numbers.txt
line_with_comment = 0
line_with_numbers = 0
comment_counter = 0
sum_of_all_numbers = 0
boolean = True

while boolean == True:
    filename = input("Enter filename (blank to exit): ") # This will ask the user to input the file name.
    filename.strip()  # This will clear all blank spaces from left and right sides.
    if len(filename) == 0:
        boolean = False
        break
    elif os.path.exists(filename) is False:
        print("Invalid filename: " + str(filename))
        stop_all = 1
    elif os.path.exists(filename):
        stop_all = 0
        # Open the random_numbers.txt and call it "random_numbers_file":
        with open(filename) as random_numbers_file:
            for line in random_numbers_file:
                """
                Determines lines without a comment symbol. 
                Which in this case is lines that only has a number. 
                """
                if "#" not in line:
                    line_with_numbers += 1
                    number = line.strip()
                    number = int(number)
                    sum_of_all_numbers += number
                """
                Determine lines that contains a comment
                """
                if "#" in line:
                    comment_counter += 1

    lines_with_comment = comment_counter
    if stop_all == 0:
        average = sum_of_all_numbers / line_with_numbers
    label_spacing = 10
    num_spacing = 10

    if stop_all == 0:
        output_line_with_numbers = str(round(line_with_numbers, 2))
        output_lines_with_comment = str(round(lines_with_comment, 2))
        output_sum_of_all_numbers = str(round(sum_of_all_numbers, 2))
        output_average = str(round(average, 2))

        # Output (Rounded to 2 Decimal Places with Padding)
        print(pad_right("Count: ", label_spacing) + pad_left(output_line_with_numbers, num_spacing))
        print(pad_right("Comments: ", label_spacing) + pad_left(output_lines_with_comment, num_spacing))
        print(pad_right("Total: ", label_spacing) + pad_left(output_sum_of_all_numbers, num_spacing))
        print(pad_right("Average: ", label_spacing) + pad_left(output_average, num_spacing))

        # Close the opened file.
        random_numbers_file.close()





