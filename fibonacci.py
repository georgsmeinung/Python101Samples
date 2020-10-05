"""
Fibonacci Numbers
-----------------
Write a function that computes the list of the first 
100 Fibonacci numbers. The first two Fibonacci numbers 
are 1 and 1. The n+1-st Fibonacci number can be computed 
by adding the n-th and the n-1-th Fibonacci number. 
The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8.
"""

def calculateSerie(terms=100):
    serie=list()
    serie.append(1)
    serie.append(1)
    while len(serie)<terms:
        serie.append(serie[-1]+serie[-2])
    return serie

print("Fibonacci Numbers")
print("-----------------")
print(calculateSerie())