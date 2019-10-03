# Loops
# for loop
# range (0, 2): starts at 0 and loops for 2 records after automatically creating the array [0,1]
# for index in range (0, 2):
# then indent 4 spaces - print(index)

people = ['Rick', 'Carrie']
print()
for name in people:
    print(name)
print()


# while loop
# be sure to change the condition or you will get stuck in the loop forever and get a stack overflow error
names = ['Rick', 'Carrie']
index = 0
while index < len(names):
    print(names[index])
    # Change the condition!
    index = index + 1
print()
