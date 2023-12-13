# Name: Adama Sylla
# Program: Chapter 5 - Loops
# Description: This software allows the user to submit three numeric test scores, checks each test result to be in a spectrum of 0-100, 
#              removes the smallest test result, computes the average of the remaining two highest test scores,
#              and generates the associated character grade based on the grading algorithm.

# CONSTANTS
title = "Welcome to Test Grade Calculator Program\n"
line = '.' * len(title)
num_tests = 3
a_grade = 90
b_grade = 80
c_grade = 70
d_grade = 60

# Print program title
print(title + line)

# Input and validate test scores
scores = []
for i in range(num_tests):
    valid = False
    while not valid:
        score = int(input(f"Enter test score {i + 1} between 0 and 100: "))
        if score >= 0 and score <= 100:
            scores.append(score)
            valid = True
        else:
            print("ERROR! Invalid score. Please enter a score between 0 and 100.")

# Find the lowest test score
lowest_score = scores[0]
for score in scores[1:]:
    if score < lowest_score:
        lowest_score = score

# Calculate average after dropping the lowest score
total = sum(scores) - lowest_score
average_score = total / (num_tests - 1)

# Determine letter grade based on average score
if average_score >= a_grade:
    letter_grade = 'A'
elif average_score >= b_grade:
    letter_grade = 'B'
elif average_score >= c_grade:
    letter_grade = 'C'
elif average_score >= d_grade:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the results
print(f"\nLowest test score dropped: {lowest_score}")
print(f"Average test score: {average_score:.2f}")
print(f"Letter grade: {letter_grade}")
