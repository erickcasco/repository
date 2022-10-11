def problem7():
    my_string = []
    num_str = int(input("Please enter how many words you would like to have entered: "))
    for i in range(num_str):
        my_string.append(input("Please enter word: "))
    my_string.sort()
    print("The words you entered were: ", my_string)
    print("The sorted words are:")
    print(*my_string, sep = "\n")
    yes_no = input("Would you like to restart the function?: ")
    if yes_no == "no":
        main()
    elif yes_no == "yes":
        problem7()
        
def main():
    problem7()

if __name__ == "__main__"
    main()
