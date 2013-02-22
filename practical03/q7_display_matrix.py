#filename: q7_display_matrix.py
#author: YuGin, 5C23
#created: 20/02/13
#modified: 22/02/13
#objective: Write a function which displays an n by n matrix where n is an
#           integer entered by the user and each element is randomly generated
#           to be either 0 or 1.

#main

import random

#function
def print_matrix(n):
    #set number of rows to print
    for i in range(1, n+ 1):
        j = ''
        #set number of elements in each row
        for i in range(1, n + 1):
            j += str("{0:<2}".format(random.randint(0, 1)))
        print(j)
    
#prompt input of integer from user
integer = int(input("Enter an integer: "))
print_matrix(integer)
