"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    score=0
    special_chr_set=["[","@","_","!","#","$","%","^","&","*","(",'"',")","<",">","?","/","|","}","{","~",":","]","'"]
    digit_set=["1","2","3","4","5","6","7","8","9","0"]
    password=input("Please enter a new password. ")

    pw_len=len(password)
    pw_correct_len=False
    pw_upper=False
    pw_lower=False
    pw_special_chr=False
    pw_digit=False

    for i in range(len(password)):
        if password[i] in special_chr_set:
            pw_special_chr=True
        else:
            pass

        if password[i] in digit_set:
            pw_digit=True
        else:
            pass

    for i in range(len(password)):
            password[i].isupper()
            if password.isupper() == True:
                pw_upper=True
            else:
                pass

    for i in range(len(password)):
            password[i].islower()
            if password.islower() == True:
                pw_lower=True
            else:
                pass

    if pw_len > 7:
            pw_correct_len=True
            score+=1
    else:
            pass

    if pw_correct_len == True:
            score+=1
    else:
            pass

    if pw_upper == True:
            score+=1
    else:
            pass

    if pw_lower == True:
            score+=1
    else:
            pass

    if pw_digit == True:
            score+=1
    else:
            pass

    if pw_special_chr == True:
            score+=1
    else:
            pass

    if score == 0 or score == 1:
          print("Weak password.")
    elif score == 2 or score == 3:
          print("Medium password.")
    elif score == 4:
          print("Strong password.")
    else:
          print("Error!")

    #Note to self, you can check all conditions in one For loop.

    pass


if __name__ == "__main__":
    main()
