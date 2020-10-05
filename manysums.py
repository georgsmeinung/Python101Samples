"""
Many types of sums
------------------
Write three functions that compute the sum of the 
numbers in a list: using a for-loop, a while-loop 
and recursion.
"""

from random import seed
from random import randint
from datetime import datetime

def generateList(maxlistlen=32):
    numset = list()
    seed(datetime.now())
    listlen = randint(1,maxlistlen)
    while len(numset)<listlen:
        seed(datetime.now())
        numset.append(randint(1,maxlistlen))
    return numset

def forSum(setOfNumbers):
    sum=0
    for i in range(len(setOfNumbers)):
        sum+=setOfNumbers[i]
    return sum

def whileSum(setOfNumbers):
    sum=0
    total=len(setOfNumbers)-1
    current=0
    while current<=total:
        sum+=setOfNumbers[current]
        current+=1
    return sum

def recursiveSum(setOfNumbers):
    sum=0
    currentLen=len(setOfNumbers)
    if currentLen>0:
        sum+=setOfNumbers[currentLen-1]
        sum+=recursiveSum(setOfNumbers[0:currentLen-1])
    return sum

print("Many types of sums")
print("------------------")
listOfNumbers=generateList()
print("The random list is:",listOfNumbers,end="\n\n")
print("For Sum is:",forSum(listOfNumbers))
print("While Sum is:",whileSum(listOfNumbers))
print("Recursive Sum is:",recursiveSum(listOfNumbers))
