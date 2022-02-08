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
    
def rps_game():
    computer = random.choice(["r" , "p" , "s"])
    user = input("Choose Rock(R), Paper(P) or Scissor(S) ").lower()

    if computer == user:
        return f"Tie, we both choose {abreviation(user)}"
    
    if winer(computer , user):
            return f"Hurray, I won. I choose {abreviation(computer)} and you choose {abreviation(user)}"
    
    return (f"Oops, I lost. I choose {abreviation(computer)} and you choose {abreviation(user)}")

print(rps_game())
