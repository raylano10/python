import random

playerOne_wins = 0

cpu_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    
    playerOne_wins = input("Type Steen/Papier/Schaar or Q om te stoppen: ").lower()

    if playerOne_wins == "q":
        break


    if playerOne_wins not in choices:
        continue
    

    random_number = random.randint(0, 2)         # steen is 0, papier is 1, schaar is 2
    cpu_pick = choices[random_number]
    print("Cpu chose", cpu_pick + ".")



    if playerOne_wins == "steen" and cpu_pick == "schaar":
        print("je hebt gewonnen!")
        playerOne_wins += 1


    elif playerOne_wins == "papier" and cpu_pick == "steen":
        print("je hebt gewonnen!")
        playerOne_wins += 1


    elif playerOne_wins == "schaar" and cpu_pick == "papier":
        print("je hebt gewonnen!")
        playerOne_wins += 1


    else:
        print("je hebt verloren!")
        cpu_wins += 1


print("je hebt", playerOne_wins, "keer gewonnen.")
print("de cpu heeft", cpu_wins, "keer gewonnen.")
print("de ballen!")