def problem1():
    count = input("Please input the number you want to see counted up to: ")
    count = int(count)
    countlist = 1
    total = 0
    while count <= 0:
        print("Error pick a number greater than 0")
        counting = input("Please input a the number you want to see counted up to: ")
    print(countlist, end='')
    total = total + countlist
    countlist = countlist + 1
    for i in range(count - 1):
        print(",",countlist, end='')
        total = total + countlist
        countlist = countlist + 1
    print("")
    print("total = ", total)
    main()
def problem2():
    count = input("Please input an integer value: ")
    count = int(count)
    countsidenum = 0
    while count <= 0:
        print("Error pick a number greater than 0")
        counting = input("Please input a the number you want to see counted up to: ")
    stars = count ** 2
    for i in range(count):
        for i in range(count):
            print("*  ", end='')
        countsidenum = countsidenum + 1
        print("  ", countsidenum)
        print("")
    print("Stars displayed = ", stars)
    main()
def problem3():
    count = input("Please input an integer value: ")
    count = int(count)
    countsidenum = 0
    stars = 0
    while count <= 0:
        print("Error pick a number greater than 0")
        counting = input("Please input a the number you want to see counted up to: ")
    for i in range(count):
        stars = stars +  1
        for i in range(stars):
            print("*  ", end='')
        print("  ", stars)
        print("")
    for i in range(count - 1):
        stars = stars - 1
        for i in range(stars):
            print("*  ", end='')
        print("  ", stars)
        print("")
    main()
def problem4():
    maxLines = input("PLease input the max number of starts per line: ")
    maxLines = int(maxLines)
    print("Part I")
    line = 0
    for i in range(maxLines):
        line = line + 1
        for i in range(line):
            print(line, end='')
        print("  ",line)
    for i in range(maxLines - 1):
        line = line - 1
        for i in range(line):
            print(line, end='')
        print("  ", line)
    print("Part II")
    line = maxLines + 1
    for i in range(maxLines):
        line = line - 1
        for i in range(line):
            print(line, end='')
        print("  ", line)
    for i in range(maxLines - 1):
        line = line + 1 
        for i in range(line):
            print(line, end='')
        print("  ", line)
    main()
def calculateParkingFee():
    print("Parking Fee")
    customers = input("Please enter the amount of customers: ")
    customers = int(customers)
    total = 0
    customer = 0
    for i in range(customers):
        hours = input("Please enter hours parked: ")
        hours = int(hours)  
        if hours <= 0:
            print("Error please enter a valid amount of hours greater than 0") 
            hours = input("Please enter hours parked: ")
            hours = int(hours)
        if hours >= 2:
            money = (hours - 1) + 3
        else:
            money = 3
        if money > 12:
            money = 12
        total = total + money
        customer = customer + 1
        print("Customer #", customer , end=' ')
        print("Hours parked: ", hours , end=' ')
        print("Total: $",money)
    print("Total amount owed: $", total)
    main()
def main():
    redirect = input("what problem do you want to be redirected to (Problem 1 = 1, Problem 2 = 2 Problem 3 = 3, Problem 4 = 4, Problem 5 = 5): ")
    if redirect == "1":
        problem1()
    elif redirect == "2":
        problem2()
    elif redirect == "3":
        problem3()
    elif redirect == "4":
        problem4()
    elif redirect == "5":
        calculateParkingFee()
if __name__ == "__main__":
    main()
