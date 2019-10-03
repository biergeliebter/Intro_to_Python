# A student makes honor roll if their average is >=85 and their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)
# True and False without quotes are boolean variables within Python
if gpa >= .85 and lowest_grade >= .70:
    honor_roll = True
else:
    honor_roll = False

# Somewhere later in the code if you need to check if the student is on honor roll, just check the boolean variable set here

if honor_roll:
    print('You made honor roll!')    