"""
Pi Approximation by serie
-------------------------
Write a program that computes the sum of an alternating 
series where each element of the series is an expression 
of the form ((-1)^{k+1})/(2 * k-1) for each value of k 
from 1 to a million, multiplied by 4. 
"""

from datetime import datetime

def showProgress(progress):
    totallen=50
    currentln=int(progress*totallen)
    print ("[{0:.<50}] {1:.0f}%".format('#'*currentln, progress*100),end="\r")
    if currentln==totallen: print("")

def makeCalculation():
    sum=0
    init = 1
    end = 10 ** 6
    startime = datetime.now()
    print ("Calculation started at {}".format(startime))
    print ("Calculating with {:.0e} serie terms...".format(end))
    showProgress(0)
    for k in range(init,end+1):
        term = ((-1)**(k+1))/(2*k-1)
        if k % (end/100) == 0:
            showProgress((k/end))
        sum += term
    sum *= 4

    endtime = datetime.now()
    difftime = endtime-startime
    difftime = difftime.total_seconds()
    timeelapsed = divmod(difftime,60)
    print ("Calculation ended at {}".format(endtime))
    print ("Calculation took {} minutes {} seconds".format(timeelapsed[0],timeelapsed[1]))
    print("The sum is {}".format(sum))

def main():
    print ("Pi Approximation by serie")
    print ("-------------------------")
    makeCalculation()

if __name__=="__main__":
    main()