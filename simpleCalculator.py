# addition function gets defined
def addition(): 
    # asks for numbers the user wants to add
    print("please enter two number which you would like to add:")
    num1 = input("input the first number: ")
    num2 = input("input the second number: ")
    # makes the user input into an int from str
    num1int = int(num1)
    num2int = int(num2)
    # calculates total
    total = num1int + num2int
    print("the total of the two numbers added is:", total)
    # makes a variable for yes or no questions
    yes_no = input("would you like to keep on adding? yes or no: ")
    # if statement redirects user
    if yes_no == "yes":
        addition()
    elif yes_no == "no":
        main()
# subtraction function gets defined       
def subtraction():
# asks for numbers the user wants to subtract
    print("please enter two number which you would like to subtract:")
    num1 = input("input the first number: ")
    num2 = input("input the second number: ")
    # makes the user input into an int from str
    num1int = int(num1)
    num2int = int(num2)
    # calculates total
    total = num1int - num2int
    print("the total of the two numbers subtracted is:", total)
    # makes a variable for yes or no questions
    yes_no = input("would you like to keep on subtracting? yes or no: ")
    # if statement redirects user
    if yes_no == "yes":
        subtraction()
    elif yes_no == "no":
        main()
# multiplication function gets defined
def multiplication():
# asks for numbers the user wants to multiply
    print("please enter two number which you would like to multiply:")
    num1 = input("input the first number: ")
    num2 = input("input the second number: ")
    # makes the user input into an int from str
    num1int = int(num1)
    num2int = int(num2)
    # calculates total
    total = num1int * num2int
    print("the total of the two numbers multiplied is:", total)
    # makes a variable for yes or no questions
    yes_no = input("would you like to keep on multiplying? yes or no: ")
    # if statement redirects user
    if yes_no == "yes":
        multiplication()
    elif yes_no == "no":
        main()    
# division function gets defined
def division():
    # asks for numbers the user wants to divide
    print("please enter two number which you would like to divide:")
    num1 = input("input the numerator number: ")
    num2 = input("input the denominator number: ")
    # makes the user input into an int from str
    num1int = int(num1)
    num2int = int(num2)
    # calculates total
    # handles dividing by 0 error
    if num2int == 0:
        print("error can't divide by a denominator of 0")
        yes_no = input("would you like to keep on dividing? yes or no: ")
        # if statement redirects user
        if yes_no == "yes":
            division()
        elif yes_no == "no":
            main()
    total = num1int / num2int
    print("the product of the two numbers divided is:", total)
    # makes a variable for yes or no questions
    yes_no = input("would you like to keep on dividing? yes or no: ")
    # if statement redirects user
    if yes_no == "yes":
        division()
    elif yes_no == "no":
        main()
# remainder function gets defined
def remainder():
    # asks for numbers the user wants to divide and get the remainder of
    print("please enter two number which you would like to divide and get the remainder of:")
    num1 = input("input the numerator number: ")
    num2 = input("input the denominator number: ")
    # makes the user input into an int from str
    num1int = int(num1)
    num2int = int(num2)
    # calculates total
    # handles dividing by 0 error
    if num2int == 0:
        print("error can't divide by a denominator of 0")
        yes_no = input("would you like to keep on dividing getting the remainder? yes or no: ")
        # if statement redirects user
        if yes_no == "yes":
            remainder()
        elif yes_no == "no":
            main()
    total = num1int % num2int
    print("the remainder of the two numbers divided is:", total)
    # makes a variable for yes or no questions
    yes_no = input("would you like to keep on dividing getting the remainder? yes or no: ")
    # if statement redirects user
    if yes_no == "yes":
        remainder()
    elif yes_no == "no":
        main()
# integer division function gets defined
def integer_division():
    # asks for numbers the user wants to divide
    print("please enter two number which you would like to integer divide:")
    num1 = input("input the numerator number: ")
    num2 = input("input the denominator number: ")
    # makes the user input into an int from str
    num1int = int(num1)
    num2int = int(num2)
    # calculates total
    if num2int == 0:
        print("error can't divide by a denominator of 0")
        yes_no = input("would you like to keep on integer dividing? yes or no: ")
        # if statement redirects user
        if yes_no == "yes":
            integer_division()
        elif yes_no == "no":
            main()
    total = num1int // num2int
    print("the product of the two numbers integer divided is:", total)
    # makes a variable for yes or no questions
    yes_no = input("would you like to keep on integer dividing? yes or no: ")
    # if statement redirects user
    if yes_no == "yes":
        integer_division()
    elif yes_no == "no":
        main()
# exponentation function gets defined
def exponentation():
# asks for numbers the user wants for exponentation
    print("please enter two number which you would like for exponentation:")
    num1 = input("input the base number: ")
    num2 = input("input the exponent number: ")
    # makes the user input into an int from str
    num1int = int(num1)
    num2int = int(num2)
    # calculates total
    total = num1int ** num2int
    print("the total of the two numbers exponentiated is:", total)
    # makes a variable for yes or no questions
    yes_no = input("would you like to keep on exponentiating? yes or no: ")
    # if statement redirects user
    if yes_no == "yes":
        exponentation()
    elif yes_no == "no":
        main()    
# average function gets defined
def average():
# asks for numbers the user wants the average of
    amount = input("how many numbers would you like to get the average of?: ")
    amountint = int(amount)
    if amountint == 0:
        print("error can't take the average of 0 numbers")
        yes_no = input("would you like to keep on averaging? yes or no: ")
        # if statement redirects user
        if yes_no == "yes":
            average()
        elif yes_no == "no":
            main()
    print("one number will be entered at a time")
    num = []
    for i in range(amountint):
        num.append(input("which number would you like to take the average of?: "))
    totalnum = list(map(int, num))
    totalnumint = sum(totalnum)
    total = totalnumint / amountint
    num.sort()
    print("the average being calculated is: ", total)
    print("the numbers averaged: ", num)
    yes_no = input("would you like to keep on averaging? yes or no: ")
    # if statement redirects user
    if yes_no == "yes":
        average()
    elif yes_no == "no":
        main()   
def exit():
    print("power off")
# main function gets defined
def main():
    # welcomes and gives all the menu options
    print("Power On")
    print("Welcome to the main menu!")
    print("Please select one of the following options:")
    print("addition")
    print("subtraction")
    print("multiplication")
    print("division")
    print("remainder")
    print("integer division")
    print("exponentation")
    print("average")
    print("exit")
    # creates variable to hold the user input
    answer = input("Please input the options exactly the way it is above capitalization counts: ")
    # if statements to redirect user based on input
    if answer == "addition":
        addition()
    elif answer == "subtraction":
        subtraction()
    elif answer == "multiplication":
        multiplication()
    elif answer == "division":
        division()
    elif answer == "remainder":
        remainder()
    elif answer == "integer division":
        integer_division()
    elif answer == "exponentation":
        exponentation()
    elif answer == "average":
        average()
    elif answer == "exit":
        exit()
if __name__ == "__main__":
    main()
