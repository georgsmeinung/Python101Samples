"""
Palindrome detector
-------------------
Write a function that tests whether a string is a palindrome.
"""

def isPalindrome(scanword):
    scanword=scanword.upper()
    palindrome=True
    wordlen = len(scanword)-1
    halflen = wordlen // 2
    for i in range(halflen):
        if scanword[i] != scanword[-(i+1)]: palindrome=False
    return(palindrome)

def main():
    print("Palindrome detector")
    print("-------------------")
    word = input("Enter a string to check: ")
    if isPalindrome(word): print("The string is a palindrome!")
    else: print("That string isn't a palindrome!")

if __name__=="__main__":
    main()