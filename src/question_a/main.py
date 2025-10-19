#add import
from question_a import get_assessment_value, get_tax_assessed

def main():

    running = True
    while running:
        print("MAIN MENU")
        print("1 - Calculate property assessment value and tax")
        print("2 - Exit")
        selection = input("Enter menu selection here: ")
        print("")
        if selection == "1":
            print("Property Value assessment and tax assessment calculator")
            property_value = float(input("Enter property value $: "))
            assessment_value = get_assessment_value(property_value)
            property_tax = get_tax_assessed(assessment_value)

            if property_value < 0:
                print("Property value cannot be less than 0")

            elif get_assessment_value(property_value):
                print(f"The assessed value of the property is ${assessment_value:.2f}")
                get_tax_assessed(property_tax)
                print(f"The property tax is ${property_tax:.2f}")
                print("")
        elif selection == "2":
            print("Exiting the program.")
            print("")
            break
        else:
            print("Error, enter valid menu selection")
            print("")

main()