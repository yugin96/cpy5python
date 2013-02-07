#filename: q04_determine_leap_year.py
#author: YuGin, 5C23
#created: 29/01/13
#modified: 29/01/13
#objective: Takes user input as a year and determine whether it is a leap year

#main

#prompt for user input of a year
year = int(input('Enter a year: '))

#check whether entered year is a leap year
if year % 4 == 0:
    if year % 100 != 0:
        print('Leap')
    else:
        if year % 400 == 0:
            print('Leap')
        else:
            print('Non-Leap')
else:
    print('Non-Leap')
                 
