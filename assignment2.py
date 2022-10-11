def numeric_comparison():
    num1str = input("Please input the first number you would like to have compared: ")
    num2str = input("Please input the second number you would like to have compared: ")
    num1 = int(num1str)
    num2 = int(num2str)
    if num1 > num2:
        print(num1, "is greater than",  num2)
    elif num1 < num2:
        print(num1, "is less than", num2)
    elif num1 == num2:
        print(num1, " is equal to", num2)
def main():
    pass
if __name__ == "__main__":
    numeric_comparison()
