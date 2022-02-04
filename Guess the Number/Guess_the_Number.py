import random

def guess(x):
    random_number = random.randrange (1, x+1)
    print(f"The number I choose is between 1 and {x}. ")
    print("Can you guess what number it is? Let's try ")
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input("Guess: "))
        if guess_number > random_number:
            print("make another guess, this time choose a smaller number ")
            
        elif guess_number < random_number::
            print("make another guess, this time choose a bigger number ")


    if guess_number == random_number:
        print (f"Well done, you did it! Correct number is {random_number}")


def comp_guess(x):
    print(f"Select a number between 1 and {x} and let's see if I can guess it")
    low , high = 1 , x
    feedback = " "

    while feedback != "y":
        if low == high:
            guess_number = low
        else:
            guess_number = random.randint( low , high )
        
        feedback = input(f"is {guess_number} correct number(Y), high(H) or low(L) ").lower()
        if feedback == "h":
            high = guess_number - 1
        elif feedback == "l":
            low = guess_number + 1
        
    if feedback == "y":
            print (f"Hurrayyyyyyyy, I did it!, correct number is {guess_number}")    


x = int(input("Enter a number: "))
guess(x)
comp_guess(x)