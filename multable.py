"""
Multiplication tables
---------------------
Write a program that prints a 
multiplication table for numbers up to 12.
"""

print("Multiplication tables")
print("---------------------")
is_integer = True
n = input ("Please enter a number: ")
try:
    n = int(n)
except:
    is_integer= False
    print("This program only works with integer numbers")
if is_integer:
    for i in range(1,13):
        print (n,"*",i,"=",n*i)
