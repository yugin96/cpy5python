#filename: q6_find_ascii_char.py
#author: YuGin, 5C23
#created: 22/01/13
#modified: 22/01/13
#objective: Take as input an ASCII code and output the corresponding character

#main

#prompt input of ASCII code
ascii_code = int(input('Enter ASCII code:'))

#reject input if input is not a valid ASCII code
if ascii_code > 127:
    print('error')

#convert ASCII to corresponding character
ascii_char = chr(ascii_code)

#display character
print(ascii_char)
