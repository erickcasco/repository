import assignment4Module1 
import assignment4Module2 
import assignment4Module3 
import assignment4Module4 
import assignment4Module5 
def main():
    print("drivers_license")
    print("numeric_comparison")
    print("letter_grade")
    print("time_in_month")
    print("time_lived")
    answer = input("Please select from the options above what you'd like to do: ")
    if answer == "drivers_license":
        assignment4Module1.drivers_license()
    elif answer == "numeric_comparison":
        assignment4Module2.numeric_comparison()
    elif answer == "letter_grade":
        assignment4Module3.letter_grade()
    elif answer == "time_in_month":
        assignment4Module4.time_in_month()
    elif answer == "time_lived":
        assignment4Module5.time_lived()
    else:
        print("Error: Invalid Input")
        main()
if __name__ == "__main__":
    main()
