"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    numbers=[]
    num=0

    while num != "stop":
            num = input("Enter your numbers ")
            try:
                num = int(num)
                numbers.append(num)
                print(numbers)
            except ValueError:
                print("You have entered text")

    def find_min():
        min=numbers[0]
        for i in range(len(numbers)):
                if numbers[i] < min:
                    min=numbers[i]
                else:
                     pass
        print(min,"is the lowest value.")

    def find_max():
        max=numbers[0]
        for i in range(len(numbers)):
                if numbers[i] > max:
                    max=numbers[i]
                else:
                     pass
        print(max,"is the highest value.")

    find_min()
    find_max()
    
    pass


if __name__ == "__main__":
    main()
