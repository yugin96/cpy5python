#filename: q3_miles_to_kilometre.py
#author: YuGin, 5C23
#created: 21/01/13
#modified: 21/01/13
#objective: Take a user input value of distance in miles and return the corresponding value in kilometres

#main

#prompt user input of distance in miles
miles = float(input("Enter distance in miles:"))

#convert distance to kilometres
kilometres = float(miles * 1.60934)

#display distance in kilometres
print("Distance = " + '{0:.2f}'.format(kilometres) + " km")
