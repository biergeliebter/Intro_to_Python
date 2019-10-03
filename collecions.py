# These are dictionaries. They are used to store key/value pairs. Storage order is not guaranteed.
rick = {}
rick['first'] = 'Rick'
rick['last'] = 'Harris'

carrie = {'first': 'Carrie', 'last': 'Harris'}

print()
print(rick)
print(carrie)
# This is a list. They have a 0 based index and storage order is guaranteed.
# An array stores simple types such as numbers. The values must all be the same type. Stored by using name=array('d') where d is digits.
people = [rick, carrie]
# Note that we stored the dictionaries we created above in this list
print(people)
people.append({'first': 'Bill', 'last': 'Gates'})
# Another common operation is list.insert(0, 'Bill') where the value gets inserted before the specified index
# Another is list.sort() Which will wort them in alphabetical order

presenters = people[0:2]
# Here we are getting a subrange of people. The first number says where to start, the second says how many records.
print(people)
print('There are ' + str(len(people)) + ' records in the people list')
# Calling the len function will get the length of a list or array
print()
print(presenters)
print('There are ' + str(len(presenters)) + ' records in the presenters list')
