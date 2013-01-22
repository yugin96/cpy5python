#filename: q5_upper_to_lower.py
#author: YuGin, 5C23
#created: 22/01/13
#modified: 22/01/13
#objective: Takes an uppercase character in standard input form and converts it to a lowercase letter by making use of its ASCII value

#main

#prompt input of a character in standard input
uppercase = input('Enter uppercase character:')

#reject input if input is not an uppercase character
if ord(uppercase) < 65:
    print('error')
if ord(uppercase) > 90:
    print('error')

#convert to ASCII value
uppercase_number = ord(uppercase)

#convert to value of corresponding lowercase character
lowercase_number = uppercase_number + 32

#convert lowercase ASCII value to character
lowercase = chr(lowercase_number)

#print lowercase character
print(lowercase)

                
