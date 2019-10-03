# print timestamps to see how long sections of code take to run
import datetime
# A cleaner way is to do from datetime import datetime then below you only need datetime.now
first_name = 'Rick'
print('task completed')
print(datetime.datetime.now())
print()

for x in range(0,10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()
# Anytime you copy the same lines of code to other places in your program, consider using a function
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()

first_name = 'Rick'
print_time()

for x in range(0,10):
    print(x)
print_time()

# pass in task name as a parameter
def print_time2(task_name):
    print(task_name)
    print(datetime.datetime.now())
    print()

first_name = 'Rick'
print_time2('first name assigned')

for x in range(0,10):
    print(x)
print_time2('loop completed')


first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]
last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial + last_name_initial)

# Another way to do this is to first create a function
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
