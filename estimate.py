def main():
    get_input()
    estimate(sqft, price_gallon)
def get_input():
    global sqft
    global price_gallon
    sqft = int(input('Enter the number of square feet to be painted: '))
    price_gallon = int(input('Enter the price of the paint per gallon: '))
def estimate(sqft, price_gallon):
    num_gallons = sqft/112
    hours_labor = num_gallons * 8
    total_price_gallon = num_gallons * price_gallon
    total_labor = hours_labor * 35
    final_total = total_price_gallon + total_labor
    print ('The total estimated price for this paint job is $', "{:.2f}".format(final_total))
main()
