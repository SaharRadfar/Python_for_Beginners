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
            
        else:
            print("make another guess, this time choose a bigger number ")


    if guess_number == random_number:
        print (f"Well done, you did it! Correct number is {random_number}")


x = int(input("Enter a number: "))
guess(x)
