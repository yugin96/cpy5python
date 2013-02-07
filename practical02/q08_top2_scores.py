#filename: q08_top2_scores.py
#author: YuGin, 5C23
#created: 29/01/13
#modified: 30/01/13
#objective: Take as input a number of students' names and their scores, and return the names of the students with the two highest scores.
#additional objective: If multiple students have either the top or second-from-top score, return all their names, up to a maximum of five joint-top or
#                      joint-second-from-top scorers


#main

#prompt input of number of students
n = int(input('Enter number of students: '))

#prompt input of individual students and their scores
i = 1
student_list_1 = []
student_list_2 = []
unsorted_score_list = []
sorted_score_list = []

#compile student names and score into separate lists
while i <= n:
    student_i = input('Enter name of student ' + str(i) + ' : ') 
    score_i = int(input('Enter score of student ' + str(i) + ' : '))
    student_list_1.append(student_i)
    student_list_2.append(student_i)
    unsorted_score_list.append(score_i)
    sorted_score_list.append(score_i)
    i = i + 1


#sort scores in increasing order
sorted_score_list.sort()

#extract top scores
highest_score = sorted_score_list.pop()

#if multiple students have the same top score, find the number of students with that score
number_joint_top = (1 + sorted_score_list.count(highest_score))

#remove top score(s) from list
i = 1
while i < number_joint_top:
    sorted_score_list.pop()
    i = i + 1

#extract second-from-top score
second_highest_score = sorted_score_list.pop()

#if multiple students have the same second-from-top score, find the number of students with that score
number_joint_second_top = (1 + sorted_score_list.count(second_highest_score))

#if there is only one student with the top score, return name of student
if number_joint_top == 1:
    highest_score_position = unsorted_score_list.index(highest_score)
    top_scorer = student_list_1.pop(highest_score_position)
    print('Top scorer is ' + top_scorer + '.')
    
#if there are multiple students with the top score, return names of all such students
if 1 < number_joint_top <= 5:
    highest_score_position_1 = unsorted_score_list.index(highest_score)
    highest_score_position_2 = unsorted_score_list.index(highest_score, highest_score_position_1 + 1)
    top_scorer_1 = student_list_1.pop(highest_score_position_1)
    top_scorer_2 = student_list_1.pop(highest_score_position_2 - 1)
    if number_joint_top > 2:
        highest_score_position_3 = unsorted_score_list.index(highest_score, highest_score_position_2 + 1)
        top_scorer_3 = student_list_1.pop(highest_score_position_3 - 2)
        if number_joint_top > 3:
            highest_score_position_4 = unsorted_score_list.index(highest_score, highest_score_position_3 + 1)
            top_scorer_4 = student_list_1.pop(highest_score_position_4 - 3)
            if number_joint_top > 4:
                highest_score_position_5 = unsorted_score_list.index(highest_score, highest_score_position_4 + 1)
                top_scorer_5 = student_list_1.pop(highest_score_position_5 - 4)

if number_joint_top == 2:
    print('Joint-top scorers are ' + top_scorer_1 + ' and ' + top_scorer_2 + '.')
if number_joint_top == 3:
    print('Joint-top scorers are ' + top_scorer_1 + ', ' + top_scorer_2 + ' and ' + top_scorer_3 + '.')
if number_joint_top == 4:
    print('Joint-top scorers are ' + top_scorer_1 + ', ' + top_scorer_2 + ', ' + top_scorer_3 + ' and ' + top_scorer_4 + '.')
if number_joint_top == 5:
    print('Joint-top scorers are ' + top_scorer_1 + ', ' + top_scorer_2 + ', ' + top_scorer_3 + ', ' + top_scorer_4 + ' and ' + top_scorer_5 + '.')
if number_joint_top > 5:
    print('Error: Too many joint-top scorers!')

#if there is only one student with the joint-second-from-top score, return name of student
if number_joint_second_top == 1:
    second_highest_score_position = unsorted_score_list.index(second_highest_score)
    second_top_scorer = student_list_2.pop(second_highest_score_position)
    print('Second-from-top scorer is ' + second_top_scorer + '.')
    
#if there are multiple students with the second-from-top score, return names of all such students
if 1 < number_joint_second_top <= 5:
    second_highest_score_position_1 = unsorted_score_list.index(second_highest_score)
    second_highest_score_position_2 = unsorted_score_list.index(second_highest_score, second_highest_score_position_1 + 1)
    second_top_scorer_1 = student_list_2.pop(second_highest_score_position_1)
    second_top_scorer_2 = student_list_2.pop(second_highest_score_position_2 - 1)
    if number_joint_second_top > 2:
        second_highest_score_position_3 = unsorted_score_list.index(second_highest_score, second_highest_score_position_2 + 1)
        second_top_scorer_3 = student_list_2.pop(second_highest_score_position_3 - 2)
        if number_joint_second_top > 3:
            second_highest_score_position_4 = unsorted_score_list.index(second_highest_score, second_highest_score_position_3 + 1)
            second_top_scorer_4 = student_list_2.pop(second_highest_score_position_4 - 3)
            if number_joint_second_top > 4:
                second_highest_score_position_5 = unsorted_score_list.index(second_highest_score, second_highest_score_position_4 + 1)
                second_top_scorer_5 = student_list_2.pop(second_highest_score_position_5 - 4)

if number_joint_second_top == 2:
    print('Joint-second-from-top scorers are ' + second_top_scorer_1 + ' and ' + second_top_scorer_2 + '.')
if number_joint_second_top == 3:
    print('Joint-second-from-top scorers are ' + second_top_scorer_1 + ', ' + second_top_scorer_2 + ' and ' + second_top_scorer_3 + '.')
if number_joint_second_top == 4:
    print('Joint-second-from-top scorers are ' + second_top_scorer_1 + ', ' + second_top_scorer_2 + ', ' + second_top_scorer_3 + ' and ' + second_top_scorer_4 + '.')
if number_joint_second_top == 5:
    print('Joint-second-from-top scorers are ' + second_top_scorer_1 + ', ' + second_top_scorer_2 + ', ' + second_top_scorer_3 + ', ' + second_top_scorer_4 + ' and ' +
          second_top_scorer_5 + '.')
if number_joint_second_top > 5:
    print('Error: Too many joint-second-from-top scorers!')


    
    



   
                        
        
