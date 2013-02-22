#name: q5_compute_series.py
#author: YuGin, 5C23
#created: 21/02/13
#modified: 22/02/13
#objective: Write a function that computes the following series: 4( 1 - 1/3
#           + 1/5 - 1/7 + 1/9 - 1/11 + 1/13... + 1 / (2i - 1) - 1 / (2i + 1)
#           where i is an integer entered by the user.

#main

#function
def compute_series(i):
    result = 0
    j = 1
    while j <= i:
        result = float(result + (1 / ((2 * j) - 1)) - (1 / ((2 * j) + 1)))
        j = j + 2
    return(4 * result)

#program to print table
print("i     m(i)")
k = 1
while k <= 19:
    print("{0:<6}".format(str(k)) + str("{0:.11f}".format(compute_series(k))))
    k = k + 2

