# A student makes honor roll if their average is >=85 and their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))
if gpa >= .85 and lowest_grade >= .70:
    print('You made the honor roll!')
else:
    print('Not too bad. Try a little harder next year and you could make honor roll.')    