import random
from words import word_list

def computer_word_list(computer_word):
    print(computer_word)
    comp_word_list = []
    for i in computer_word:
        comp_word_list.append(i)

    return (comp_word_list)

def hangman():
    computer_word = random.choice(word_list)
    word = computer_word_list(computer_word)
    print("This is Hangman game, I will select a word and let's see if you can guess what it is")
    print(f"let's start, my word had {len(word)} letters")
    user_word = []
    show_word = []

    while set(user_word) != set(word):
        letter = input ("Guess a letter: ")
        if letter in word:
            user_word.append(letter)
            print (f"Correct, '{letter}' is letter {word.index(letter)+1} in my word")
        else:
            print ("nice try, guess again!")

    print(f"Well done, you did it. my word is {computer_word}")


hangman()
