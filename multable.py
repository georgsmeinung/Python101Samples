"""
Multiplication tables
---------------------
Write a program that prints a 
multiplication table for numbers up to 12.
"""

def checkInteger(inputNumber):
    num = None
    try:
        num = int(inputNumber)
    except:
        print("Only integer numbers allowed!")
        num = False
    return num

def printTable(number):
    for i in range(1,13): print (number,"*",i,"=",number*i)

def main():
    print("Multiplication tables")
    print("---------------------")
    n = input ("Please enter a number: ")
    n = checkInteger(n)
    if n: printTable(n)

if __name__=="__main__":
    main()