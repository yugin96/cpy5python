#filename: q6_determine_prime.py
#author: YuGin, 5C23
#created: 19/02/13
#modified: 22/02/13
#objective: Write a function to determine if a number is prime. Display the
#           first 1000 prime numbers in rows of 10.

#main

#function to determine if number is prime
def is_prime(n):
    determinant = 'unknown'
    for i in range (2, n):
        if n % i == 0:
            determinant = False
            #break out of 'for' loop once number is proven to be prime
            break 
    if determinant == False:
        return(False)
    else:
        return(True)

#program to print first 1000 prime numbers
    
#initialize empty string to contain prime numbers
j = '' 
k = 0
for n in range (2, 10001): #estimate for range of first 1000 prime numbers
    if is_prime(n) == True:
        j += (str("{0:<5}".format(n)))
        #print row j and start new row if j contains 10 numbers
        if len(j) == 50: 
            print(j) 
            j = '' 
        k = k + 1
    if k > 1000:
        break
