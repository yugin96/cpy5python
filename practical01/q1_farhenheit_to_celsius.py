#filename: q1_fahrenheit_to_celsius.py
#author: YuGin, 5C23
#created: 21/01/13
#modified: 22/01/13
#objective: convert user input value of a temperature in Farenheit and output equivalent value in Celsius

#main

#prompt input of temperature in Fahrenheit from user
Fahrenheit = float(input('Enter temperature in Fahrenheit: '))

#convert value in Fahrenheit to degrees Celsius
Celsius = (5/9) * (Fahrenheit - 32)

#display value in degrees Celcius
print("Temperature = " + '{0:.2f}'.format(Celsius) + " degrees Celsius")
