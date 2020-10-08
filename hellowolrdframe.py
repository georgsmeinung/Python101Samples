"""
Hello World in a frame
----------------------
Write a function that takes a list of strings and 
prints them, one per line, in a rectangular frame. 
For example the list 
["Hello", "World", "in", "a", "frame"] 
gets printed as:
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
"""

def getLargestElement(scanlist):
    maxlen=0
    for i in scanlist:
        if len(i)>maxlen: 
            maxlen=len(i)
    return maxlen

def drawFrame(message):
    maxwidth=getLargestElement(message)+4
    print("*"*maxwidth)
    for i in range(len(message)):
        print("* {:^{width}} *".format(message[i],width=(maxwidth-4)))
    print("*"*maxwidth)

def toList(stringMsg):
    outList=list(stringMsg.split(" "))
    return outList

def main():
    print("Hello World in a frame")
    print("----------------------")
    text=input("Enter a message: ")
    text=toList(text)
    drawFrame(text)

if __name__=="__main__":
    main()