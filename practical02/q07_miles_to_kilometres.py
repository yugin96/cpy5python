#filename: q07_miles_to_kilometres.py
#author: YuGin, 5C23
#created: 29/01/13
#modified: 29/01/13
#objective: Display two tables side by side: One shows values of 1-10 miles and their corresponding values in kilometres; the other shows values of 20-65 kilometres
#           in intervals of 5 km and their corresponding values in miles.

#main

#print heading
print('Miles Kilometres  Kilometres Miles')

#print values in table
i = 1
j = 20
while i <= 10:    
    print("{0:<6s}".format(str(i)) + str("{0:<12.3f}".format(i * 1.609)) + "{0:<11s}".format(str(j)) + str("{0:3f}".format(i / 1.609)))
    i = i + 1
    j = j + 5
          
