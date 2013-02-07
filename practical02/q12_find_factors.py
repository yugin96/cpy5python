#filename: q12_find_factors.py
#author: YuGin, 5C23
#created: 30/01/13
#modified: 30/01/13
#objective: Takes as input an integer and returns all the smallest factors of that integer

#main

#prompt user input of an integer
n_original = int(input('Enter an integer: '))
n = n_original

#find smallest factors and compile them into a list
f = 2
list_of_factors = []
while n > 1:
    while n % f == 0:
        list_of_factors.append(f)
        n = n / f
    f = f + 1

#arrange list of factor in increasing order
list_of_factors.sort()

#return list of factors
print('Smallest factors of ' + str(n_original) + ': ' + str(list_of_factors))
