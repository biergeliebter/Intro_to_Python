# Ctrl+K+C to comment a line, Ctrl+K+U to uncomment a line
# input function always returns strings
# To get current date and time we need to use the datetime library
from datetime import datetime, timedelta
# The now cuntion returns a datetime object
Today = datetime.now()
print("Today is " + str(Today))
one_day = timedelta(days=1)
yesterday = Today - one_day
print("Yesterday was " + str(yesterday))

current_date = datetime.now()
print("Today is " + str(current_date))
one_week = timedelta(weeks=1)
last_week = Today - one_week
print("Last week was " + str(last_week))
print("Day " + str(Today.day))
print("Month " + str(Today.month))
print("Year " + str(Today.year))
print("Hour " + str(Today.hour))
print("Minute " + str(Today.minute))
print("Second " + str(Today.second))

UserBirthday = input("When is your birthday? (dd/mm/yyyy) ")
birthday_date = datetime.strptime(UserBirthday, '%d/%m/%Y')
print("Birthday " = str(birthday_date))