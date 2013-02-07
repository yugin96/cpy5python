#filename: q06_kilograms_to_pounds.py
#author: YuGin, 5C23
#created: 29/01/13
#modified: 29/01/13
#objective: Display a table which shows values of 1-10 kilograms and the corresponding mass in pounds

#main

#print heading
print('Kilograms Pounds')

#print values of 1-10 kilograms and corresponding mass in pounds
i = 1
while i <= 10:    
    print("{0:<10s}".format(str(i)) + str("{0:1f}".format(i * 2.2)))
    i = i + 1
