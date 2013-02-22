#filename: q2_display_pattern.py
#author: YuGin, 5C23
#created: 16/02/13
#modified: 22/02/13
#objective: Writes a function that displays a pattern based on an integer

#main
def display_pattern(n):
    i = 1
    j = ' '
    if n >= 10: #specific formatting for pattern with n >= 10
        k = 2 * n - 9
        l = - 1 - (n - 10)
        while i <= n:
            number_line = ("{0:{1}}" + str(i) + ' '  + j).format('', 2 * k + l) 
            print(number_line)
            j = str(i) + ' ' + j
            i = i + 1
            if i >= 10:
                k = k - 2
                l = l + 1
            else:
                k = k - 1
    else: #specific formatting for pattern with n < 10
        k = n 
        while i <= n:
            number_line = ("{0:{1}}" + str(i) + ' ' + j).format('', 2 * k) 
            print(number_line)
            j = str(i) + ' ' + j
            i = i + 1
            k = k - 1
              
#prompt user to input integer
integer = int(input('Enter an integer: '))
display_pattern(integer)
