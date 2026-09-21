"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    shopping_list=[]
    item=input("Please enter an item to add to your list. ")
    item_position_str=True

    while item.lower() != "done":
        shopping_list.append(item)
        item=input("Please enter an item to add to your list.")

    choice=input("Would you like to edit any items? (Y/N) ")

    if choice.lower() == "y":
        print("Your shopping list:",shopping_list)
        item_position=input("Please enter the number that describes the position of the item you would like to edit. The first item is in position 0. ")
        while item_position_str == True:
            try:
                item_position=int(item_position)
                item_position_str=False
            except:
                item_position_str=input("Please enter a number. ")

        change=input("Please enter what you would like to change the item with. ")

        shopping_list[item_position]=change

    print()
    print("Your shopping list:",shopping_list)
    pass


if __name__ == "__main__":
    main()
