# Ask for someone's name and return the initials

first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]
middle_name = input('Enter your middle name: ')
middle_name_initial = middle_name[0:1]
last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial + middle_name_initial + last_name_initial)

# Another way to do this is to first create a function
# This function will return the first initial
def get_initial(name):
    initial = name[0:1].upper()
    return initial
    # return means to always pass a value back

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)
# Function get_initial runs for first_name, returning a value, and we store that value as first_name_initial
last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial + last_name_initial)

# We can get even fancier with the code
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print('Your initials are: ' + get_initial(first_name) + get_initial(last_name))