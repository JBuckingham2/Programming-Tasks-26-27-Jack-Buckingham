"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    exit=False
    while exit == False:
        print("Type the number of the option you would like to pick")
        print("1. Farenheit to Celsius")
        print("2. Celsius to Farenheit")
        print("3. Exit")
        choice=input("Please enter your choice. ")

        try:
            choice=int(choice)
        except:
            print("You have entered a letter!")

        if choice == 1:
            f=float(input("Enter the temperature in Farenheit. "))
            c=(f-32)*5/9
            print(f,"farenheit is equal to",c,"celcius. ")
        elif choice == 2:
            c=float(input("Enter the temperature in Celsius. "))
            f=(c*9/5)+32
            print(c,"celsius is equal to",f,"farenheit. ")
        elif choice == 3:
            print("Exiting now...")
            exit=True
        else:
            print("That is not an option.")
    pass


if __name__ == "__main__":
    main()
