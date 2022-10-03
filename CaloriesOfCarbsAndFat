def main():
    get_input()
    caloriesDisplay(fatCalories, carbsCalories)
def get_input():
    global fatCalories
    global carbsCalories
    fat = int(input("Enter the grams of fat: "))
    while fat < 0:
        print("Error: Invalid Input")
        fat = int(input("Enter the grams of fat: "))
    fatCalories = fat * 9
    carbs = int(input("Enter the grams of carbs: "))
    while carbs < 0:
        print("Error: Invalid Input")
        carbs = int(input("Enter the grams of carbs: "))
    carbsCalories = carbs * 4
def caloriesDisplay(fatCalories, carbsCalories):
    print("The calories from fat are: ", "{:.2f}".format(fatCalories))
    print("The calories from carbs are: ", "{:.2f}".format(carbsCalories))
main()
