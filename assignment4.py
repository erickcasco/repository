def time_in_month():
    print("Please input the month in a number format, ex. 1 = January, 10 = October.")
    monthstr = input("Which month would you like to know how much time there is in it?: ")
    month = int(monthstr)
    if month == 1:
        days = 31
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is January.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 2:
        print("The month chosen is February.")
        yes_no = input("Is this year a leap year? (yes or no): ")
        if yes_no == "yes":
            days = 29
        elif yes_no == "no":
            days = 28
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 3:
        days = 31
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is March.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 4:
        days = 30
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is April.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 5:
        days = 31
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is May.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 6:
        days = 30
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is June.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 7:
        days = 31
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is July.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 8:
        days = 30
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is August.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 9:
        days = 30
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is September.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 10:
        days = 31
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is October.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 11:
        days = 30
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is November.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    elif month == 12:
        days = 31
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print("The month chosen is December.")
        print("days = ", days)
        print("hours = ", hours)
        print("minutes = ", minutes)
        print("seconds = ", seconds)
    else:
        print("Invalid month please reenter what month you would like to check the time in that month")
        time_in_month()
def main():
    pass
if __name__ == "__main__":
    time_in_month()
