"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    def get_multiples(number):
        for i in range(1,13):
            answer=number*i
            print(str(i),"x",str(number),"=",str(answer))
    number=int(input("Enter a number. "))
    get_multiples(number)
    pass


if __name__ == "__main__":
    main()

