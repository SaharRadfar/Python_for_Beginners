import random

def winer(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

def abreviation(argument):
    if argument == "r":
        return "Rock"
    elif argument == "s":
        return "Scissor"
    elif argument == "p":
        return "Paper"
    
def rps_game(user_score,computer_score):
    print(f"You: {user_score} - Computer: {computer_score}")
    while user_score != 5 and computer_score != 5:
        user = input("What's your choice? Rock(R), Paper(P) or Scissor(S) ").lower()
        computer = random.choice(["r" , "p" , "s"])
        
        while user not in user_input:
            print (f"You: {user_score} - Computer: {computer_score}")
            print("Wrong input, try again")
            user = input("Choose Rock(R), Paper(P) or Scissor(S) ").lower()

        if computer == user:
            print (f"Tie, we both choose {abreviation(user)}")
        
        if winer(computer , user):
                computer_score += 1
                print (f"I choose {abreviation(computer)} and you choose {abreviation(user)}")
                
        
        if winer(user , computer):
            print (f"I choose {abreviation(computer)} and you choose {abreviation(user)}")
            user_score += 1
    
    if user_score > computer_score :
        print (f"Oops, I lost the game")
        print(f"final Score: You: {user_score} - Computer: {computer_score}")
    
    else:  
        print (f"Hurray, I won the game")
        print(f"final Score: You: {user_score} - Computer: {computer_score}")    

user_score = 0
computer_score = 0
user_input = ["r" , "s" , "p"]

rps_game(user_score,computer_score)