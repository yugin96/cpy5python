#filename: q09_find_smallest.py
#author: YuGin, 5C23
#created: 30/01/13
#modified: 30/01/13
#objective: Find the smallest integer, n, such that n^2 > 12,000.

#main

n = 12000
while (n * n) > 12000:
    n = n - 1
print(n)
