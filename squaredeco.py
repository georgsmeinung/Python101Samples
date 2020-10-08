"""
Square decorator
----------------
rite a function on_all that applies a function to
every element of a list. Use it to print the first
twenty perfect squares. The perfect squares can be
found by multiplying each natural number with itself.
The first few perfect squares are 1*1= 1, 2*2=4, 
3*3=9, 4*4=16. Twelve for example is not a perfect 
square because there is no natural number m so that 
m*m=12. 
"""

def showSquare(func):
    def PrintSquare(number):
        print ("Number is {} and square is {}".format(number, func(number)))
    return PrintSquare
    
@showSquare
def calculateSquare(num):
    return num**2

def main():
    print("Square decorator")
    print("----------------")
    squaresToCalculate=20
    for i in range(1,squaresToCalculate+1):
        calculateSquare(i)

if __name__=="__main__":
    main()