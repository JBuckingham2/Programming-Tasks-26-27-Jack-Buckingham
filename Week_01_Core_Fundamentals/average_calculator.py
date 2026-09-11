"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    number=0
    mean=0
    total=0
    list=[]
    num=0
    while num != "Stop":
        num = input("Enter your numbers")
        try:
            num = int(num)
            list.append(num)
            print(list)
        except:
            print("You have entered text")

    
    lennum=len(num)
    for i in range (lennum-1):
        total = total + list[i]
        number = number + 1
    total = total / lennum
    print(total)
    pass



if __name__ == "__main__":
    main()
