#filename: q4_sum_series.py
#author: YuGin, 5C23
#created: 17/02/13
#modified: 22/02/13
#objective: Write a function that computes the following series: m(i) = (1/2)+
#           (2/3) + ... + (i/i+1).

#main

#function
def m_series(i):
    j = 1
    sum = 0
    while j <= i:
        sum = float(sum + (j / (j + 1)))
        j = j + 1
    return(sum)

#program to print table
print("i          m(i)")
for k in range (1, 21):
    print("{0:<11}".format(str(k)) + str("{0:.4f}".format(m_series(k))))
    
