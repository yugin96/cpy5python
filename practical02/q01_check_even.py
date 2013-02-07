#filename: q01_check_even.py
#author: YuGin, 5C23
#created: 29/01/13
#modified: 29/01/13
#objective: takes an integer input by a user and checks whether it is even or odd

#main

#prompt integer input from user
integer = int(input('Enter an integer: '))

#check if integer is even and return result to user
if integer % 2 == 0:
    print(str(integer) + ' is even')
else:
    print(str(integer) + ' is odd')



