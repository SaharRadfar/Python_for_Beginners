import random
from words import word_list

def hangman():
    word = random.choice(word_list).upper()
    user_word = []
    used_letter = []
    show_word = [letter if letter in used_letter else "-" for letter in word]
    
    print("This is Hangman game, I will select a word and you should guess it.")
    print (f'Current word is {" ".join(show_word)}')

    while set(user_word) != set(word):
        print("")
        print (f'You have used following letters: {", ".join(used_letter).upper()}')
        letter = input ("Guess a letter: ").upper()
        
        if letter in used_letter:
            print (f"You have already used {letter} Character, try another one.")
        
        elif letter in set(word):
            user_word.append(letter)
            used_letter.append(letter)
            show_word = [letter if letter in used_letter else "-" for letter in word]
            print (f'Correct. Current word is {" ".join(show_word)}')
            
        else:
            print (f'nice try, guess again! Current word is {" ".join(show_word)}')
            used_letter.append(letter)
            

    print("")
    print(f"Well done, you did it. my word is {word}")
    print("")


hangman()