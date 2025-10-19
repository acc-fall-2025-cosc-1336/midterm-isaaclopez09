#add import
from question_d import is_prime

def main():
        running = True
        while running:
            print("MAIN MENU")
            print("1 - Prime number calculator")
            print("2 - Exit")
            selection = input("Enter menu selection here: ")
            print("")
            if selection == "2":
                 print("Exiting the program")
                 break
            elif selection == "1":
                try:
                    number = int(input("Enter number to check if it is prime: "))
                    print("")
                    if is_prime(number):
                        print(f"{number} is a prime number.")
                    else:
                        print(f"{number} is NOT a prime number.")
                except ValueError:
                    print("Please enter a valid integer or 'q' to quit.")

                print("")
            else:
                print("Error, enter valid menu selection")
                print("")

            
main()
                  
