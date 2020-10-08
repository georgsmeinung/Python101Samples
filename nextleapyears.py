"""
Leap year calculation
---------------------
Write a program that prints the next 20 leap years.
"""

from datetime import date

def calculateNextLeapYears(n,current):
    leapYears = list()
    current+=1

    while len(leapYears)<n:
        if current % 4 == 0:
            if current % 100 == 0:
                if current % 400 == 0:
                    leapYears.append(current)
            else:
                leapYears.append(current)
        current+=1

    print(leapYears)

def main():
    today = date.today()
    print("Today is {}".format(today))
    currentYear = today.strftime("%Y")
    currentYear = int(currentYear)
    leapsAhead = 20

    print("Leap year calculation")
    print("---------------------")
    print("Next {} leap years after {}:".format(leapsAhead,currentYear))
    calculateNextLeapYears(leapsAhead,currentYear)

if __name__=="__main__":
    main()