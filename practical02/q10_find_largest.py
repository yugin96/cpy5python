#filename: q10_find_largest.py
#author: YuGin, 5C23
#created: 29/01/13
#modified: 29/01/13
#objective: Find the largest integer n such that n^3 is less than 12,000.

#main

n = 1
while (n * n * n) < 12000:
    n = n + 1
print(n)
