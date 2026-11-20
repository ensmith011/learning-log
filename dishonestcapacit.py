print('Enter TB or GB for the adverttsed unit:')
unit = input('>')

# Calculate teh amount that the advertised capicty lies:
if unit =='TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capcity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# Calculate the real capcity, round it to the nearest hundredths,
# and conver it tot a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)