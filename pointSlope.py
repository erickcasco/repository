#function for y = mx + b
def main():
    variable = int(input("What variable would you like to solve for? 1 = y 2 = m 3 = x 4 = b: "))
    if variable > 4 or variable < 1:
        print("Error: Invalid Input")
        variable = int(input("What variable would you like to solve for? 1 = y 2 = m 3 = x 4 = b"))
        while variable > 4:
            print("Error: Invalid Input")
            variable = int(input("What variable would you like to solve for? 1 = y 2 = m 3 = x 4 = b"))
            while variable < 1:
                print("Error: Invalid Input")
                variable = int(input("What variable would you like to solve for? 1 = y 2 = m 3 = x 4 = b"))
        while variable < 1:
            print("Error: Invalid Input")
            variable = int(input("What variable would you like to solve for? 1 = y 2 = m 3 = x 4 = b"))
            while variable > 4:
                print("Error: Invalid Input")
                variable = int(input("What variable would you like to solve for? 1 = y 2 = m 3 = x 4 = b"))
    if variable == 1:
        yVar()
    elif variable == 2:
        mVar()
    elif variable == 3:
        xVar()
    else: 
        bVar()
def yVar():
    m = float(input("Enter m variable value: "))
    x = float(input("Enter x variable value: "))
    b = float(input("Enter b variable value: "))
    y = (m * x) + b
    print("y =", y)
def mVar():
    x = float(input("Enter x variable: "))
    b = float(input("Enter b variable: "))
    y = float(input("Enter y variable: "))
    m = ((-1 * b) + y) / x
    print("m =", m)
def xVar():
    b = float(input("Enter b variable: "))
    y = float(input("Enter y variable: "))
    m = float(input("Enter m variable: "))
    x = ((-1 * b) + y) / m
    print("x =", x)
def bVar():
    y = float(input("Enter y variable: "))
    m = float(input("Enter m variable: "))
    x = float(input("Enter x variable: "))
    b = ((m * x) * -1) + y
    print("b =", b)
main()
