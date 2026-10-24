## Build Client Name and Hour and hourly rate calculator

print('Client Name:')
client_name = input('>')
print('Hours Worked:')
hours_worked = input('>')
print('Hourly Rate:')
hourly_rate = input('>')
print('Client Name: ' + client_name)
print('Hours Worked: ' + hours_worked)
print('Hourly Rate: ' + hourly_rate)
total_earning = float(hours_worked) * float(hourly_rate)
print('Total Earnings: ' + str(total_earning))