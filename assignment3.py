def letter_grade():
    print("User's letter grade will be calculated 5 assignment grades are needed.")
    num1str = input("Please input the first grade you would like to have compared: ")
    num1 = int(num1str)
    if num1 > 100:
        print("Error: Assignment grade can not be over 100%")
        print("Please restart entering grades!")
        letter_grade()
    if num1 < 0:
        print("Error: Assignment grade can not be under 0%")
        print("Please restart entering grades!")
        letter_grade()
    num2str = input("Please input the second grade you would like to have compared: ")
    num2 = int(num2str)
    if num2 > 100:
        print("Error: Assignment grade can not be over 100%")
        print("Please restart entering grades!")
        letter_grade()
    if num2 < 0:
        print("Error: Assignment grade can not be under 0%")
        print("Please restart entering grades!")
        letter_grade()
    num3str = input("Please input the third grade you would like to have compared: ")
    num3 = int(num3str)
    if num3 > 100:
        print("Error: Assignment grade can not be over 100%")
        print("Please restart entering grades!")
        letter_grade()
    if num3 < 0:
        print("Error: Assignment grade can not be under 0%")
        print("Please restart entering grades!")
        letter_grade()
    num4str = input("Please input the fourth grade you would like to have compared: ")
    num4 = int(num4str)
    if num4 > 100:
        print("Error: Assignment grade can not be over 100%")
        print("Please restart entering grades!")
        letter_grade()
    if num4 < 0:
        print("Error: Assignment grade can not be under 0%")
        print("Please restart entering grades!")
        letter_grade()
    num5str = input("Please input the fifth grade you would like to have compared: ")
    num5 = int(num5str)
    if num5 > 100:
        print("Error: Assignment grade can not be over 100%")
        print("Please restart entering grades!")
        letter_grade()
    if num5 < 0:
        print("Error: Assignment grade can not be under 0%")
        print("Please restart entering grades!")
        letter_grade()
    inputTotal = num1 + num2 + num3 + num4 + num5
    letterGrade = inputTotal / 5
    print("Your letter grade is: ", letterGrade)
    if letterGrade < 60:
        print("Your letter grade is an F")
    elif letterGrade < 70:
        print("Your letter grade is a D")
    elif letterGrade < 80:
        print("Your letter grade is a C")
    elif letterGrade < 90:
        print("Your letter grade is a B")
    elif letterGrade <= 100:
        print("Your letter grade is an A")
def main():
    pass
if __name__ == "__main__":
    letter_grade()
