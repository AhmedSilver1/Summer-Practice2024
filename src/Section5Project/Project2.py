import time

#Asking input from the user:
sleepHours = input("How many hours you sleep? ")
workHours = input("How may hours you work? ")
relaxPerWorkdayHours = input("How many hours you rest in work week? ")
relaxPerWeekendHours = input("How many hours you rest in weekend? ")

#Computing Study hours:
studyHoursPerWeekWork = 24 - (int(sleepHours) + int(workHours) + int(relaxPerWorkdayHours) + 3)
studyHoursPerWeekend = 24 - (int(sleepHours) + int(relaxPerWeekendHours) + 3)
studyHoursPerWeek = (int(studyHoursPerWeekWork) * 5) + (int(studyHoursPerWeekend) * 2)

#Printing

print("your study hours per work day is: " + str(studyHoursPerWeekWork))
time.sleep(2)
print("your study hours per weekend day is: " + str(studyHoursPerWeekend))
time.sleep(2)
print("your total study hours per week is : " + str(studyHoursPerWeek))
