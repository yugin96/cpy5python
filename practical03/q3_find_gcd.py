#filename: q3_find_gcd.py
#author: YuGin, 5C23
#created: 17/02/13
#modified: 22/02/13
#objective: Write a function that finds the greatest common divisor of two
#           positive integers

#main
def gcd(m, n):
    i = 2
    divisor = 1
    while i <= m and i <= n:
        #test for both m and n to be divisible by i
        if m % i == 0:
            if n % i == 0:
                divisor = i
        i = i + 1
    return(divisor)

print('Greatest common divisor of 24 and 16 = ' + str(gcd(24, 16)))
print('Greatest common divisor of 255 and 25 = ' + str(gcd(255, 25)))

