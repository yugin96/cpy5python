#filename: q03_determine_grade.py
#author: YuGin, 5C23
#created: 29/01/13
#modified: 29/01/13
#objective: Takes a score as input from user and returns the corresponding grade.

#main

#prompt user input of score
score = float(input('Enter a score from 1-100: '))

#match score to corresponding grade
if 69.5 <= score <= 100:
    grade = 'A'
if 59.5 <= score <= 69.4:
    grade = 'B'
if 54.5 <= score <= 59.4:
    grade = 'C'
if 49.5 <= score <= 54.4:
    grade = 'D'
if 44.5 <= score <= 49.5:
    grade = 'E'
if 34.5 <= score <= 44.4:
    grade = 'S'
if 0 <= score <= 34.4:
    grade = 'U'

#output grade
if 0 <= score <= 100:
    print(grade)

#display error message if input score is out of range
if score > 100:
    print('Invalid! Score must be within 0 - 100.')
else:
    if score < 0:
        print('Invalid! Score must be within 0 - 100.')
