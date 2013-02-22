#filename: q1_display_reverse.py
#author: YuGin, 5C23
#created: 16/02/13
#modified: 16/02/13
#objective: Writes a function that displays an integer in reverse

#main



#create empty string
reverse = ''

def reverse_int(integer):
    
    reverse = ''

#arrange digits in reverse order and add to empty string
    while len(str(integer)) > 0:           
        reverse += (str(integer))[-1]
        integer = str(integer)[:-1]

#print result
    print(int(reverse)) #int formatting removes extra zeros at start of result
          
#prompt user to input integer
number = int(input('Enter an integer: '))
reverse_int(number)
