# Keys must be immutable. Which means you can use strings,
# numbers or tuples as dictionary keys but something like ['key'] is not allowed. Following is a simple example:
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print ("dict['Name']: ", dict['Name'])
print ("dict['Class']: ", dict['Class'])
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

print(len(dict))
print(len(dict))
print(len(dict))
print()
