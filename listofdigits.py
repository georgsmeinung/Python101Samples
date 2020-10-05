"""
List of digits
--------------
Write a function that takes a number and returns 
a list of its digits. 
So for 2342 it should return [2,3,4,2].
"""

def getDigits(number):
    digits=list()
    while number>10:
        digits.append(number%10)
        number//=10
    else:
        digits.append(number)
    return digits[::-1]

num = input("Enter an integer number: ")
try:
    num = int(num)
    print(getDigits(num))
except:
    print("Only integer numbers allowed!")
    