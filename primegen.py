"""
Eratosthenes primes sieve
-------------------------
Write a program that prints all prime numbers. (Note: if your 
programming language does not support arbitrary size numbers, 
printing all primes up to the largest number you can easily 
represent is fine too.)
"""

print("Eratosthenes primes sieve")
print("-------------------------")
is_integer = True
n = input ("Please the highest number to find primes: ")
try:
    n = int(n)
except:
    is_integer= False
    print("This program only works with integer numbers")
if is_integer:    
    numbers=list(range(2,n+1))
    # print(numbers)
    comp=0
    i=0
    while i<len(numbers):
        j=i
        while j<len(numbers):
            comp+=1
            if (numbers[j]>numbers[i]) and (numbers[j] % numbers[i] == 0): 
                numbers.pop(j)
            else: j+=1
        else:
            i+=1
    print(numbers)
    print("In",comp,"ops")

