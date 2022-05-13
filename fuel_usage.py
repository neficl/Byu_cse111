import math

def main():
    first_odometer = float(input("Enter the first odometer reading (miles): "))

    second_odometer = float(input("Enter the second odometer reading (miles): "))

    amount_fuel = float(input("Enter the amount of fuel used (gallons): "))

    mpg = miles_per_gallon(first_odometer, second_odometer, amount_fuel)

    lp100k = lp100k_from_mpg(mpg)
    
    print(f"{round(mpg, 1)} miles per gallon")
    print(f"{round(lp100k, 2)} liters per 100 kilometers")
    
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    
    mpg = (end_miles - start_miles)/amount_gallons
    
    return mpg


def lp100k_from_mpg(mpg):
    
    lp100k = 235.215 / mpg
    
    return lp100k

# Call the main function so that
# this program will start executing.
main()
