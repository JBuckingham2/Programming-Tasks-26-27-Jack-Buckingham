"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

#Enqueue — someone joins the back of the line
#Dequeue — the person at the front gets served and leaves (and you'd return who it was)
#Peek — look at who's at the front without removing them
#Size — how many people are waiting

def main():
    queue=["Tom","Jane","Patrick"]
    print("Would you like to:")
    print("1. Add a customer")
    print("2. Serve a customer")
    print("3. Size")
    print("4. Peek")
    print("5. Quit")
    choice=int(input("Enter the number of your choice. "))

    while choice != 5:

        if choice == 1:
            name=input("Enter the name of the new queuer. ")
            queue.append(name)
            print("Queue:",queue)

        elif choice == 2:
            print(queue[0],"has been served. ")
            queue.pop(0)
            print("New queue is",queue)

        elif choice == 3:
            size=len(queue)
            print("Queue currently has",str(size),"people in it. ")

        elif choice == 4:
            print(queue[0],"is the next customer. ")

        else:
            print("Sorry, that is not an option")

        print("Would you like to:")
        print("1. Add a customer")
        print("2. Serve a customer")
        print("3. Size")
        print("4. Peek")
        print("5. Quit")
        choice=int(input("Enter the number of your choice. "))

    pass


if __name__ == "__main__":
    main()
