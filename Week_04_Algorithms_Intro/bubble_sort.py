"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

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

    n = len(list)
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            else:
                pass

    print(list)

    pass


if __name__ == "__main__":
    main()
