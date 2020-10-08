"""
List of digits
--------------
Write a function that takes a number and returns 
a list of its digits. 
So for 2342 it should return [2,3,4,2].
"""

def checkInteger(inputNumber):
    num = None
    try:
        num = int(inputNumber)
    except:
        print("Only integer numbers allowed!")
        num = False
    return num

def getDigits(numberToScan):
    digits=list()
    while numberToScan>10:
        digits.append(numberToScan%10)
        numberToScan//=10
    else:
        digits.append(numberToScan)
    return digits[::-1]

def main():
    number = input("Enter an integer number: ")
    number = checkInteger(number)
    if number: print(getDigits(number))

if __name__=="__main__":
    main()