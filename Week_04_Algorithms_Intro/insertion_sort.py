"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def main():
    import random as r
    list = []

    list_len = r.randint(1, 10)
    for i in range(list_len):
        num = r.randint(1, 100)
        list.append(num)

    print(list)

    for i in range(1, len(list)):
        insert_index = i
        current_value = list.pop(i)
        for j in range(i-1, -1, -1):
            if list[j] > current_value:
                insert_index = j
            else:
                break
        list.insert(insert_index, current_value)

    print(list)

if __name__ == "__main__":
    main()
