#filename: q05_find_month_days.py 
#author: YuGin, 5C23
#created: 29/01/13
#modified: 29/01/13
#objective: Takes a month and a year as inputs from user, and displays the number of days in that month and in that particular year.

#main

#prompt user input of month and year
month = int(input('Enter a month from 1-12, with 1 being January and 12 and December: '))
year = str(input('Enter a year: '))

#return number of days in month if input month is not February
if month == 1:
    print('January ' + year + ' has 31 days.') 
if month == 3:
    print('March ' + year + ' has 31 days.')
if month == 4:
    print('April ' + year + ' has 30 days.')
if month == 5:
    print('May ' + year + ' has 31 days.')
if month == 6:
    print('June ' + year + ' has 30 days.')
if month == 7:
    print('July ' + year + ' has 31 days.')
if month == 8:
    print('August ' + year + ' has 31 days.')
if month == 9:
    print('September ' + year + ' has 30 days.')
if month == 10:
    print('October ' + year + ' has 31 days.')
if month == 11:
    print('November ' + year + ' has 30 days.')
if month == 12:
    print('December ' + year + ' has 31 days.')

   
#determine whether input year is a leap year if input month is February
if month == 2:
    if int(year) % 4 == 0:
        if int(year) % 100 != 0:
            print('February ' + str(year) + ' has 29 days.')
        else:
            if int(year) % 400 == 0:
                print('February ' + str(year) + ' has 29 days.')
    else:
        print('February ' + str(year) + ' has 28 days.')
    
    
