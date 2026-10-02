"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    data=[]
    print("1. Append array")
    print("2. Read array")
    print("3. Delete an entry")
    print("4. Stop")
    choice=int(input("Enter your choice. "))
    while choice != 4:

        if choice == 1:
            x=input("Enter your data. ")
            y=input("Enter your data. ")
            data.append([x,y])
            print(data)

        elif choice == 2:
            print("Your array:",data)

        elif choice == 3:
            delete=int(input("Enter the number of the element you would like to remove. "))
            delete-=1
            print("Entry removed:",data[delete])
            data.pop(delete)
            print("Your array now:",data)

        choice=int(input("Enter your choice. "))

    pass


if __name__ == "__main__":
    main()
