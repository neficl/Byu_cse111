age = int(input("Please enter your age: "))

maximum = (220 - age) * 0.85
minimum = (220 - age) * 0.65

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {minimum: .0f} and {maximum: .0f} beats per minute.")