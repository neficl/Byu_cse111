""""
Néfi Leite - BYUI Id: 253999429
The volume of Tire!
"""
from datetime import datetime
from math import pi


current_date = datetime.now()

width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
print()

volume = ((pi * pow(width, 2) * ratio) * (width * ratio + ( 2540 * diameter))) / 10000000000

with open ("volumes.txt", "at") as volumes_file:
    print(f"{current_date:%Y-%m-%d}, {width: .0f}, {ratio: .0f}, {diameter: .0f}, {volume: .2f}", file=volumes_file)
