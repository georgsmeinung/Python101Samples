"""
Leap year calculation
---------------------
Write a program that prints the next 20 leap years.
"""

from datetime import date

today = date.today()
print("Today is {}".format(today))
currentYear = today.strftime("%Y")
currentYear = int(currentYear)

n = 20
print("Leap year calculation")
print("---------------------")
print("Next {} leap years after {}:".format(n,currentYear))

leapYears = list()
currentYear+=1

while len(leapYears)<n:
    if currentYear % 4 == 0:
        if currentYear % 100 == 0:
            if currentYear % 400 == 0:
                leapYears.append(currentYear)
        else:
            leapYears.append(currentYear)
    currentYear+=1

print(leapYears)