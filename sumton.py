"""
Conditional Sum
---------------
Modify the previous program such that only multiples of 
three or five are considered in the sum, 
e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
"""

def checkInteger(inputNumber):
    num = None
    try:
        num = int(inputNumber)
    except:
        print("Only integer numbers allowed!")
        num = False
    return num

def is_divisible(number,divisor):
    return (number % divisor) == 0

def doConditionalSum(number):
    s = 0
    print("Adding ",end="")
    for i in range(1,number+1):
        if is_divisible(i,3) or is_divisible(i,5):
            print (i," + ",end="")
            s+=i
        if i==number: print(end="\b\b ")


    else: print("")
    print ("The sum of multiple of 3 and 5 from 1 to",number,"is",s)

def main():
    print("Conditional Sum")
    print("---------------")
    n = input ("Please enter a number: ")
    n = checkInteger(n)
    if n: doConditionalSum(n)

if __name__=="__main__":
    main()