"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    def get_grade(score):
        grade="Error"
        if score < 40:
            grade="D"
        elif score > 39 and score < 60:
            grade="C"
        elif score > 59 and score < 80:
            grade="B"
        elif score > 79 and score < 101:
            grade="A"
        else:
                print("Sorry, that is not a percentage between 1 and 100.")
        print("Student got grade:",str(grade))
        pass

    score=int(input("Please enter a student's precentage. "))
    get_grade(score)

if __name__ == "__main__":
    main()