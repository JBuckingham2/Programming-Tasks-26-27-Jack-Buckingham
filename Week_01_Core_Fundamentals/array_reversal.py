"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    import random
    count=0
    random_ints=[]
    rev_random_ints=[]

    while count < 5:
        int_for_random_ints=random.randint(1,9)
        random_ints.append(int_for_random_ints)
        count+=1

    for i in range(4,-1,-1):
        num=random_ints[i]
        rev_random_ints.append(num)
    pass

    print("Before:",random_ints,"After:", rev_random_ints)

if __name__ == "__main__":
    main()