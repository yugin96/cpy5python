#name: q1_sum_series1.py
#author: YuGin, 5C23
#created: 22/02/13
#modified: 22/02/13
#objective: Write a recursive function sum_series1(i) to compute the series (1 +
#           1/2 + 1/3 + ... + 1/i).

#main
def sum_series1(i):
    if i == 1:
        return(1)
    else:
        return(1 / i + sum_series1(i - 1))

#prompt user to input value for i
integer = int(input('Enter an integer: '))
print(str(sum_series1(integer)))
