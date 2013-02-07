#filename: q02_triangle.py
#author: YuGin, 5C23
#created: 29/01/13
#modified: 29/01/13
#objective: take three inputs as the lengths of the edges of a triangle and determines if the input makes a valid triangle. If so, return the perimeter of
#           the triangle; if not, display an error message.

#main

#prompt for user input of values for three edges of triangle
side_1 = int(input('Enter side 1: '))
side_2 = int(input('Enter side 2: '))
side_3 = int(input('Enter side 3: '))

#define perimeter of triangle
perimeter = side_1 + side_2 + side_3

#check to see if values form a valid triangle
if side_1 + side_2 > side_3:
    if side_1 + side_3 > side_2:
        if side_2 + side_3 > side_1:
            print('Perimeter = ' + str(perimeter)) #if all conditions are fufilled up to this point, values are valid. Print perimeter.
        else:
            print('Invalid triangle!') #if not all conditions are fufilled, values are invalid. Display error message.
    else:
        print('Invalid triangle!')
else:
    print('Invalid triangle!')
    

        
        


        
