#name: q3_find_gcd.py
#author: YuGin, 5C23
#created: 22/02/13
#modified: 22/02/13
#objective: Write a recursive function gcd(m, n) that finds the greatest common
#           divisor of the two positive integers m and n.

#main

#function
def gcd(m, n):
    if m > n:
        if m % n == 0:
            return(n)
        else:
            return(gcd(n, m % n))
    if m < n:
        if n % m == 0:
            return(m)
        else:
            return(gcd(m, n % m))

#Print gcd of 24 & 16 and 255 & 25
print('Greatest common divisor of 24 and 16 = ' + str(gcd(24, 16)))
print('Greatest common divisor of 255 and 25 = ' + str(gcd(255, 25)))
    
