#name: q6_sum_digits.py
#author: YuGin, 5C23
#created: 26/02/13
#modified: 26/02/13
#objective: Write a recursive function sum_digits(n) that computes the sum of
#           the digits in an integer n.

#main

#function
def sum_digits(n):
    #terminating case when integer is 0
    if len(str(n)) == 0:
        return 0
    else:
        return int(str(n)[0]) + sum_digits(str(n)[1:])

#prompt user input of integer
integer = input('Enter an integer: ')
print(sum_digits(integer))
