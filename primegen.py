"""
Eratosthenes primes sieve
-------------------------
Write a program that prints all prime numbers. (Note: if your 
programming language does not support arbitrary size numbers, 
printing all primes up to the largest number you can easily 
represent is fine too.)
"""

def checkInteger(inputNumber):
    num = None
    try:
        num = int(inputNumber)
    except:
        print("Only integer numbers allowed!")
        num = False
    return num

def calculatePrimes(maxNumber):
    numbers=list(range(2,maxNumber+1))
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
    print("Made in",comp,"ops")

def main():
    print("Eratosthenes primes sieve")
    print("-------------------------")
    n = input ("Please the highest number to find primes: ")
    n = checkInteger(n)
    if n: calculatePrimes(n)

if __name__=="__main__":
    main()
