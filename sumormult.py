"""
Sum or Multiply
---------------
Write a program that asks the user for a number n and 
gives them the possibility to choose between computing 
the sum and computing the product of 1,...,n.
"""

def checkInteger(inputNumber):
    num = None
    try:
        num = int(inputNumber)
    except:
        print("Only integer numbers allowed!")
        num = False
    return num

def main():
    print("Sum or Multiply")
    print("---------------")
    n = input ("Please enter a number: ")
    n = checkInteger(n)
    if n:
        op = input("Would you like to sum or multiply? (+/*):")
        if op=="+" or op=="*":
            s = 1
            print("{} {} ".format(s,op),end="")
            for i in range(2,n+1):
                if op=="+": s+=i
                if op=="*": s*=i
                print("{} ".format(i),end="")
                if i<n:print("{} ".format(op),end="")
            else: print("=")
            print ("The result is",s)
        else:
            print ("Valid operations are + or *")

if __name__=="__main__":
    main()