import random

def winer(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


def rps_game():
    computer = random.choice(["r" , "p" , "s"])
    user = input("Choose Rock(R), Paper(P) or Scissor(S) ").lower()

    if computer == user:
        return f"Tie, we both choose {user}"
    
    if winer(computer , user):
            return f"Hurray, I win. I choose {computer} and you choose {user}"
    
    return (f"Oops, I lost. I choose {computer} and you choose {user}")

print(rps_game())
