"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    print("Would you like to:")
    print("1. Enter data")
    print("2. Read file")
    choice=int(input("Enter your choice. "))

    if choice == 1:
        file=open("data.csv","w")
        name=input("Enter your name. ")
        fav_colour=input("Enter your favourite colour. ")
        age=input("Enter your age. ")
        file.write(name+","+age+","+fav_colour)

    else:
        file=open("data.csv","r")
        data=file.readlines()
        print(data)
    pass


if __name__ == "__main__":
    main()
