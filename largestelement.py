"""
Largest Element, reverse add odds
---------------------------------
Write a function that returns the largest element in a list.
Write function that reverses a list, preferably in place.
Write a function that returns the elements on odd positions in a list.
"""

from random import seed
from random import randint
from datetime import datetime

def generateList(maxlistlen=32):
    wordset = list()
    baseword = "abcdefghijklmnopqrstuvwxyz"
    seed(datetime.now())
    listlen = randint(1,maxlistlen)
    for i in range(listlen):
        wordlen = randint(1,10)
        wordset.append("")
        while len(wordset[i])<wordlen:
            selchar = randint(0,len(baseword)-1)
            wordset[i]+=baseword[selchar]
    return wordset

def getLargestElement(scanlist):
    maxlen=0
    for i in range(len(scanlist)):
        if len(scanlist[i])>maxlen: 
            maxlen=len(scanlist[i])
            maxpos=i
    return (maxlen,maxpos)

def reverseList(originalList):
    currentlen = len(originalList)-1
    halflen = currentlen // 2
    for i in range(halflen):
        originalList[i],originalList[-(i+1)]=originalList[currentlen-i],originalList[i]
    return(originalList)

def oddElements(originalList):
    oddlist = list()
    for i in range(len(originalList)):
        if (i+1) % 2 == 0:
            oddlist.append(originalList[i])
    return(oddlist)

maxlen = 32
newlist = generateList(maxlen)
largestElement = getLargestElement(newlist)

print("Largest Element, reverse add odds")
print("---------------------------------")
print("This a {} elements list: {}".format(len(newlist),newlist),end="\n\n")

print("The larges element have {} chars is in position number {} and has value \"{}\"".format(largestElement[0],largestElement[1]+1,newlist[largestElement[1]]),end="\n\n")

print("The reversed list is:",reverseList(newlist),end="\n\n")

print("The odd elements are:",oddElements(newlist),end="\n\n")