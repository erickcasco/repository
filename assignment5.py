def time_lived():
    yearsstr = input("Please input your age in years: ")
    years = int(yearsstr)
    daysstr = input("Please input the days after your last birthday that you have lived: ")
    days = int(daysstr)
    hoursstr = input("Please input the hours since the last day that you have lived: ")
    hours = int(hoursstr)
    if years > 3:
        leapyears = years // 4
    else:
        leapyears = 0
    totaltime = (years * 365 * 24 * 60 * 60) + (days * 24 * 60 * 60) + (hours * 60 * 60) + (leapyears * 24 * 60 * 60)
    print("In total you have lived ", totaltime, " seconds")
def main():
    pass
if __name__ == "__main__":
    time_lived()
