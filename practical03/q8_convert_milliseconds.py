#filename: q8_convert_milliseconds.py
#author: YuGin, 5C23
#created: 19/02/13
#modified: 22/02/13
#objective: Write a function that converts millliseconds to seconds, minutes,
#           and hours.

#main
def convert_ms(n):
    i = 3600000
    hours = 0
    #if n is worth 1 hour or more, extract number of hours
    if n >= 3600000: #3600000 ms = 1 hour
        while (n / i) >= 1:
            hours = hours + 1
            i = i + 3600000
        #remaining milliseconds after hours have been extracted
        remaining_m = n - (hours * 3600000)
    else:
        remaining_m = n

    j = 60000
    minutes = 0
    #if remaining_m is worth 1 minute or more, extract number of minutes
    if remaining_m >= 60000: #60000 ms = 1 minute
        while (remaining_m / j) >= 1:
            minutes = minutes + 1
            j = j + 60000
        #remaining milliseconds after minutes have been extracted
        remaining_s = remaining_m - (minutes * 60000)
    else:
        remaining_s = remaining_m

    k = 1000
    seconds = 0
    #if remaining_s is worth 1 second or more, extract number of seconds
    if remaining_s >= 1000: #1000 ms = 1 second
        while (remaining_s / k) >= 1:
            seconds = seconds + 1
            k = k + 1000
        remaining_ms = remaining_s - (seconds * 1000)
    else:
        remaining_ms = remaining_s
    
    print('Time (h/m/s): ' + str(hours) + ':' + str(minutes) + ':' +
          str(seconds))

#prompt user to input value for number of milliseconds
milliseconds = int(input('Enter number of milliseconds: '))
convert_ms(milliseconds)
