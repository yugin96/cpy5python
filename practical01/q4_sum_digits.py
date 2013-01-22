#filename: q4_sum_digits.py
#author: YuGin, 5C23
#created: 21/01/13
#modified: 22/01/13
#objective: Take as input an integer between 0 and 1000, and return the sum of the digits.

#main

#prompt input of integer
integer = int(input("Enter integer:"))

#extract individual digits and add them together
sum = 0
sum = sum + integer % 10
while integer % 100 != integer % 10:
    integer = integer // 10
    sum = sum + integer % 10

#return sum of digits
print(sum)
    
