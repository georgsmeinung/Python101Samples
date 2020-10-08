"""
Hello Alice or Bob
------------------
Write a program that asks the user for their name and 
greets them with their name. 
Modify the previous program such that only the users 
Alice and Bob are greeted with their names.
"""


def main():
    print ("Hello Alice or Bob")
    print ("------------------")
    name = input ("What's your name? ")
    if not((name == "Alice") or (name == "Bob")):
        name = ""
    print ("Hello",name)

if __name__=="__main__":
    main()
