"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def main():
    import random as r
    list = []

    list_len = r.randint(1, 20)
    for i in range(list_len):
        num = r.randint(1, 100)
        list.append(num)

    num_to_search = int(input("Enter a number from the list ("+str(list)+")"))

    for i in range(len(list)):
        if num_to_search == list[i]:
            position = i
        else:
            pass

    print(num_to_search, "is in position", position)


if __name__ == "__main__":
    main()
