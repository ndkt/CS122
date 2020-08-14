"""
CIS 122
Name: Ohm Sabpisal
Credit: N/A
Class: CIS 122
Date: 22 November 2019
Description: Find Palindrome and word stuff.
"""

# Initialize Variables
import string
filename = 'words_alpha.txt'
number_of_words = palindrome_count = count = 0
words_list = []
all_alphabets = list(string.ascii_lowercase)
alphabets_varible = [alph[0] for alph in all_alphabets]
alphabet_count = [0, 0,
				  0, 0,
				  0, 0,
				  0, 0,
				  0, 0,
				  0, 0,
				  0, 0,
				  0, 0,
				  0, 0,
				  0, 0,
				  0, 0,
				  0, 0,
				  0, 0]

# Search for a Palindrome Function
def reverse(word):
	return word[::-1] # This notation start from the end of the string towards the start of the string counting in -1 direction.

# Open the file
with open(filename) as file_object:
	lines = file_object.readlines()

# Find number of words in file
for line in lines:
	number_of_words += 1
	word = line.strip()
	reverse_word = reverse(word)
	words_list.append(word)
	initial_letter = line[0]

	# Check how many words is a palindrome
	if word == reverse_word:
		palindrome_count += 1

	# Letter is not in the file, add 1 to count.
	if initial_letter not in alphabets_varible:
		count += 1


	# Print out the amount of each letter.
	for i in range(26):
		if initial_letter == alphabets_varible[i]:
			alphabet_count[i] += 1

# Find shortest and longest word in the list:
shortest_word = min(words_list, key=len) # The min function has an optional parameter key that lets you specify a function to determine the "sorting value" of each item.
longest_word = max(words_list, key=len) # The max function has an optional parameter key that lets you specify a function to determine the "sorting value" of each item.

def findPercentage(value):
	""" This function calculates the percentage of input value """
	percentage = " (" + str(round(((value)/(number_of_words) * 100),2)) + "%" + ") "
	return str(percentage)


def amount_of_letter():
	"""This function will print out the amount of words with the initial alphabet beginning with the each alphabet and calculating the percentage."""
	for i in range(26):
		percentageOfLetter = str(findPercentage(alphabet_count[i]))
		print(str(alphabets_varible[i].upper()) + ": " + str(alphabet_count[i]) + str(percentageOfLetter))


# Output Value
print("Count: " + str(number_of_words))
print("Longest word is " + longest_word + " (" + str(len(longest_word)) + ")") # Find longest word in list.
print("Shortest word is " + shortest_word + " (" + str(len(shortest_word)) + ")") # Find shortest word in list.
print("Palindromes: " + str(palindrome_count) + findPercentage(palindrome_count))
amount_of_letter()
print("Other " + str(count) + findPercentage(count))
