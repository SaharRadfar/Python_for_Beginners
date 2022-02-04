import random

def user_guess(x):
    random_number = random.randrange (1, x+1)
    y = x // 10 if x % 10 == 0 else (x // 10) + 1
    print(f"The number I choose is between 1 and {x}. ")
    print("Can you guess what number it is? ")
    print(f"You have {y} chances, Let's try it")
    guess_number = 0


    answer = "wrong"
    for life in range ( 1 , y+1 ):
        guess_number = int(input("Now guess: "))
        if guess_number == random_number:
            print ("Well done, you did it!")
            answer = "correct"
            break

        else: 
            if life != y:
                if guess_number > random_number:
                    print (f"Not correct, you have {y-life} other chance to guess")
                    print("This time choose a smaller number: ")
                    
                else:
                    print (f"Wrong guess, you have {y+-life} other chance to guess")
                    print("This time choose a greater one: ")
            
    if answer == "wrong":
        print(f"Sorry, you are out of life, correct number is {random_number}!")



def comp_guess(x):
    y = x // 10 if x % 10 == 0 else (x // 10) + 1
    low , high = 1 , x
    feedback = " "
    print(f"Select a number between 1 and {x} and let's see if I can guess it")
    print(f"I'll guess {y} times, Let's start")  
    useless_parameter = input("Are you ready? ")

    for i in range ( 1 , y+1 ):
        if low == high:
            guess_number = low
        else:
            guess_number = random.randint( low , high )
        
        feedback = input(f"guess no.{i}: is {guess_number} correct number(Y), high(H) or low(L) ").lower()
        if feedback == "h":
            high = guess_number - 1
        elif feedback == "l":
            low = guess_number + 1
    
        if feedback == "y":
            print (f"Hurrayyyyyyyy, I did it!, correct number is {guess_number}")
            break
    if feedback !="y" :
        print ("Oops, I'm out of life! you win... ")  


x = int(input("Enter a number greater than 5: "))
who = ""

while who != "y" and who != "c":
    who = input("Who will Guess the number? you(M) or computer(C) ").lower()
    if who == "y":
        user_guess(x)
    elif who == "c": 
        comp_guess(x)