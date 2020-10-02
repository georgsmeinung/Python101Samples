"""
Sum or Multiply
---------------
Write a program that asks the user for a number n and 
gives them the possibility to choose between computing 
the sum and computing the product of 1,...,n.
"""

print("Sum or Multiply")
print("---------------")
is_integer = True
n = input ("Please enter a number: ")
try:
    n = int(n)
except:
    is_integer= False
    print("This program only works with integer numbers")
if is_integer:
    op = input("Would you like to sum or multiply? (+/*):")
    if op=="+" or op=="*":
        s = 1
        for i in range(2,n+1):
            if op=="+": s+=i
            if op=="*": s*=i
        print ("The result is",s)
    else:
        print ("Valid operations are + or *")
