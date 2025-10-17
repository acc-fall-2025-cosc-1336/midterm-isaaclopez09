#add import
from question_b import get_miles_per_hour

def main():
    print("Miles Per Hour Calculator")
    
    kilometers = int(input("Enter kilometers: "))
    if kilometers <= 0:
        return print("Invalid arguments: Kilometers must be greater than 0")

    minutes = int(input("Enter minutes: "))
    if minutes <= 0:
        return print("Invalid arguments: minutes must be greater than 0")


    miles_per_hour = get_miles_per_hour(kilometers, minutes)

    print(f"The speed in miles per hour is {miles_per_hour:.6f}")

main()