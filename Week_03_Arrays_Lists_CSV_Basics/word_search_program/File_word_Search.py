"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # I don't know how to download the file so I will make it work for any given file. 
    count=0
    num_lines=0
    file_name=input("Enter the file name. ")
    file=open(file_name)
    word=input("Enter the word to search. ")
    for lines in file:
        count+=1
        text=file.readline()
        text=text.lower()
        text=text.split()
        if word in text:
            print(word,"is in line",count)
            num_lines+=1
        else:
            continue
    print('"',word,'"appears in',num_lines,'lines.')
    pass


if __name__ == "__main__":
    main()
