
from datetime import datetime

current_date = datetime.now()
day_of_week = current_date.weekday()

x = 1
while(x):
    subtotal = float(input("\nPlease enter the subtotal? "))
    if subtotal == 0:
            x = 0
            print("End of your program!")
    elif subtotal >= 50 and (day_of_week == 2 or day_of_week == 3): ## Tuesday or Wednesday, compute the discount amount.
            discount = subtotal * 0.9
            print(f"You got a 10% discount, the total was: R${discount}")
    else: 
            print(f"You did not receive any discount, you will pay: R${subtotal}")

