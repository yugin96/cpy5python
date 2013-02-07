#filename: q11_find_gcd.py
#author: YuGin, 5C23
#created: 30/01/13
#modified: 30/01/13
#objective: takes user input of two integers and finds the greatest common divisor among them

#main

#prompt user input of two integers
n1 = int(input('Enter first integer: '))
n2 = int(input('Enter second integer: '))

#find greatest common divisor
if n1 > n2:
    d = n2
    while n1 % d != 0 or n2 % d != 0:
        d = d - 1
    print('Greatest common divisor of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(d) + '.')
else:
    if n2 > n1:
        d = n1
        while n1 % d != 0 or n2 % d != 0:
            d = d - 1
        print('Greatest common divisor of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(d) + '.')
    else:
        print('Greatest common divisor of ' + str(sn1) + ' and ' + str(n2) + ' is ' + str(n1) + '.')
