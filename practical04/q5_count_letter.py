#name: q5_count_letter.py
#author: YuGin, 5C23
#created: 26/02/13
#modified: 26/02/13
#objective: Write a recursive function count_letter(str, ch) that finds the
#           number of occurences of a specified leter, ch, in a string, str.

#main

#function
def count_letter(str, ch):
    #terminating case when string is empty
    if len(str) == 0: 
        return 0
    #add 1 to result if ch is equal to first character of str
    if str[0] == ch:
        return 1 + count_letter(str[1:], ch)
    #add 0 to result if ch is not equal to first character of str
    if str[0] != ch:
        return 0 + count_letter(str[1:], ch)

#prompt user input of string and character
string = str(input('Enter a string: '))
character = str(input('Enter a character: '))
print(count_letter(string, character))
