#filename: q2_calc_cylinder_volume.py
#author: YuGin, 5C23
#created: 21/01/13
#modified: 21/01/13
#objective: Take as input a cylinder's radius and length, and calculate its volume

#main

#prompt user input of length
length = float(input("Enter length of cylinder:"))

#prompt user input of radius
radius = float(input("Enter radius of cylinder:"))

#calculate base area of cylinder
from math import pi
base_area = pi * radius * radius

#calculate volume of cylinder
volume = base_area * length

#display volume of cylinder
print("Volume of cylinder = " + '{0:.2f}'.format(volume) + " cm^3")

