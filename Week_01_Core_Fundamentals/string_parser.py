"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    sentence=input("Input a sentence. ")
    words=[]
    wordcount=0
    current_word=""
    for i in range(len(sentence)):
        character=sentence[i]
        if character == " ":
            if current_word != "":
                words.append(current_word)
                current_word=""
        else:
            current_word=current_word+character
    if current_word != "":
        words.append(current_word)

    for i in range(len(words)):
        wordcount+=1

    print(words)
    print(wordcount,"words")

if __name__ == "__main__":
    main()
