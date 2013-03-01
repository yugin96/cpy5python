#name: q2_sum_series2.py
#author: YuGin, 5C23
#created: 22/02/13
#modified: 22/02/13
#objective: Write a recursive function sum_series2(i) to compute the series (1/3
#           + 2/5 + 3/7 + 4/9 + 5/11 + 6/13 + ... + i / (2i+1)).

#main

#function
def sum_series2(i):
    if i == 1:
        return(1)
    else:
        return(i / (2 * i + 1) + sum_series2(i - 1))

#prompt user to input integer
integer = int(input('Enter an integer: '))
print(sum_series2(integer))
