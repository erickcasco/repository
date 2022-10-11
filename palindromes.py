def testPalindrome():
    palindrome = input("Please enter a string for palindrome status: ")
    print("You entered: ", palindrome)
    reversedPalindome = str()
    for i in reversed(palindrome):
        reversedPalindome = reversedPalindome + i
    print("Your word reversed is: ", reversedPalindome)
    if reversedPalindome == palindrome:
        print("Yes you entered in a Palindrome")
    else: 
        print("No this is not a Palindrome")
    yes_no = input("Would you like to restart the function?: ")
    if yes_no == "no":
        main()
    elif yes_no == "yes":
        testPalindrome()
        
def main():
    testPalindrome()
 
if __name__ == "__main__":
    main()
