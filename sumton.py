"""
Conditional Sum
---------------
Modify the previous program such that only multiples of 
three or five are considered in the sum, 
e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
"""

def is_divisible(number,divisor):
    return (number % divisor) == 0


print("Conditional Sum")
print("---------------")
is_integer = True
n = input ("Please enter a number: ")
try:
    n = int(n)
except:
    is_integer= False
    print("This program only works with integer numbers")
if is_integer:
    s = 0
    for i in range(1,n+1):
        if is_divisible(i,3) or is_divisible(i,5):
            print ("Adding",i)
            s+=i
    print ("The sum of multiple of 3 and 5 from 1 to",n,"is",s)
