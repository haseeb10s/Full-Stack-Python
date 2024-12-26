userDetails = {
    'Name': 'Haseeb',
    'Email': '@gmail.com',
    'Age': 23,
    'isVerified': True
}
userDetails['Name'] = 'Jacken'
print(userDetails['Name'])
print(userDetails.get('Bithday', '4 April'))
print(userDetails)

# ex: 1
phone = input('Phone: ')
digits_mapping = {
    '1': 'One',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}
output = ''
for ch in phone:
    output += digits_mapping.get(ch, '!') + ' '
print(output)    
