def drivers_license():
    age = input("How old are you?: ")
    ageint = int(age)
    # error for being less than 0 years old
    if ageint < 0:
        print("Error: This is not a real age")
        print("Please reenter your real age!")
        drivers_license()
    # error for being too old, the oldest human was 122 years old
    if ageint > 122:
        print("Error: This is not a real age")
        print("Please reenter your real age!")
        drivers_license()
    # People over 95 can not get a license
    elif ageint >= 96:
        print("Sorry you are too old to have a drivers license!")
    # People 18 or over can get a license
    elif ageint > 17:
        print("Congraulations you can get a drivers license!")
    # People under 18 can not get a license
    elif ageint <= 17:
        print("Please wait to get your drivers license!")
def main():
    pass
if __name__ == "__main__":
    drivers_license()
