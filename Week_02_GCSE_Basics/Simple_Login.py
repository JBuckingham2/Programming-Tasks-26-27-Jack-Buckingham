"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    username="user"
    password="pw"
    password_guess_correct=False
    user_guess_two="not right"
    password_guess_two="not the password"
    guess_count=0

    user_guess=input("Enter your username. ")
    if user_guess != username:
        while user_guess_two != username:
            user_guess_two=input("That is not a registered username. Enter your correct username. ")
    else:
        pass

    print("Enter your password",user_guess)
    password_guess=input()
    if password_guess != password:
        while password_guess_correct == False and guess_count < 3:
            attempts_left=3-guess_count
            print("Access denied!",attempts_left,"atempts remaining.")
            password_guess_two=input()
            if password_guess_two == password:
                print("Welcome. ")
                password_guess_correct=True
            else:
                guess_count+=1
        print("You are locked out.")
    else:
        print("Welcome. ")
    pass


if __name__ == "__main__":
    main()