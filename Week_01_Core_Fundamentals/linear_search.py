"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    import random
    value=-69
    count=0
    random_l1st=[]

    while count < 5:
        ints_for_random_l1st=random.randint(1,9)
        random_l1st.append(ints_for_random_l1st)
        count+=1

    print(random_l1st)

    target=int(input("Please enter the target. "))
    len_random_l1st=len(random_l1st)
    for i in range(len_random_l1st):
        value=random_l1st[i]
        if value == target:
            index=i
        else:
            pass
    target=str(target)
    index=str(index)
    print(target+"'s index is",index)

if __name__ == "__main__":
    main()
