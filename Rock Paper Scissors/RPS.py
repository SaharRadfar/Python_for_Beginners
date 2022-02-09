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
    
def rps_game(user):
    computer = random.choice(["r" , "p" , "s"])

    if computer == user:
        return f"Tie, we both choose {abreviation(user)}"
    
    if winer(computer , user):
            return f"Hurray, I win. I choose {abreviation(computer)} and you choose {abreviation(user)}"
    
    return (f"Oops, I lost. I choose {abreviation(computer)} and you choose {abreviation(user)}")


user = input("Choose Rock(R), Paper(P) or Scissor(S) ").lower()
user_input = ["r" , "s" , "p"]

while user not in user_input:
    print("Wrong input, try again")
    user = input("Choose Rock(R), Paper(P) or Scissor(S) ").lower()
    
print(rps_game(user))