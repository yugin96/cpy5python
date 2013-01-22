#filename: q7_generate_payroll.py
#author: YuGin, 5C23
#created: 21/01/13
#modified: 22/01/13
#objective: Obtain a user's number of hours worked weekly, hourly pay, and CPF contribution, and hence calculate his net pay

#main

#prompt user input of name
name = input('Enter name: ')

#prompt user input of hours worked weekly
work_hours = int(input('Enter number of hours worked weekly: '))

#prompt user input of hourly pay
hourly_pay = float(input('Enter hourly pay in dollars: '))

#prompt user input of CPF contribution
CPF_rate = int(input('Enter CPF contribution rate (%): '))

#calculate gross and net weekly pay
gross_pay = hourly_pay * work_hours
net_pay = gross_pay * (1 - (CPF_rate / 100))


#calculate CPF contribution amount
CPF_amount = gross_pay * (CPF_rate / 100)


#output payroll statement
print('') 
print('Payroll statement for ' + name)
print('Number of hours worked in week: ' + str(work_hours))
print('Hourly pay rate: $' + str('{0:.2f}'.format(hourly_pay)))
print('Gross pay = $' + '{0:.2f}'.format(gross_pay))
print('CPF contribution at ' + str(CPF_rate) + '% = $' + str('{0:.2f}'.format(CPF_amount)))
print('')  
print('Net pay = $' + '{0:.2f}'.format(net_pay))
      


