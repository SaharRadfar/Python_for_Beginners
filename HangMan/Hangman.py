import random
from words import word_list

def hangman():
    word = random.choice(word_list).upper()
    user_word = []
    show_word = []
    used_letter = []
    print("This is Hangman game, I will select a word and let's see if you can guess what it is")
    print(f"let's start, my word had {len(word)} letters")

    for i in word:
        show_word.append("-")
    
    while set(user_word) != set(word):
        print (f'You have used following letters {" ".join(used_letter).upper()}')
        letter = input ("Guess a letter: ").upper()
        if letter in used_letter:
            print (f"You have already used {letter} Character, try another one.")
        
        elif letter in set(word):
            user_word.append(letter)
            used_letter.append(letter)
            print (f"Correct, '{letter}' is letter {word.index(letter)+1} in my word")

        else:
            print ("nice try, guess again!")
            used_letter.append(letter)

    print(f"Well done, you did it. my word is {word}")


hangman()
