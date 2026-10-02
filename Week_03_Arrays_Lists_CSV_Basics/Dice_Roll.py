"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    import random
    results=[]
    total=0
    count=0

    num_rolls=int(input("Enter how many times you would like the dice rolled. "))

    for i in range(0,num_rolls):
        side=random.randint(1,7)
        results.append(side)
        print("Roll",str(i+1)+":",side)
        total+=side

    average=total/len(results)
    average=round(average,0)
    print(average,"was the average roll.")

    for i in range(1,7):
        count=results.count(i)
        side_total = i * count
        print(i,"was rolled",count,"times.")
        print(i,"X",count,"=",side_total)
    
    pass


if __name__ == "__main__":
    main()
