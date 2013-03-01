#name: q8_find_uppercase.py
#author: YuGin, 5C23
#created: 03/01/13
#modified: 03/01/13
#objective: Write a recursive function find_num_uppercase(str) to return the
#           number of uppercase letters in a string str.

#main

#function
def find_num_uppercase(str):
    if len(str) == 0:
        return 0
    else:
        if str[0] == str[0].upper():
            return 1 + find_num_uppercase(str[1:])
        else:
            return 0 + find_num_uppercase(str[1:])

#prompt user to input string
string = input('Enter a string of text: ')
print(find_num_uppercase(string))
