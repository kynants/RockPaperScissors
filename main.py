import random

# Moves
moves = ["r", "p", "s"]

# Player enters move
player_move = input("Choose rock (r), paper (p), or scissors (s): ")

# Input Validation
while player_move != "r" or "p" or "s":
    player_move = input("Invalid choice. Try again: ")
    if player_move == "r" or "p" or "s":
        break

# CPU responds
cpu_move = random.choice(moves)

# Move comparison
if player_move == "r" and cpu_move == "r":
    print("It's a tie.")
elif player_move == "p" and cpu_move == "r":
    print("You win!")
elif player_move == "s" and cpu_move == "r":
    print("You lose.")
elif player_move == "r" and cpu_move == "p":
    print("You lose.")
elif player_move == "p" and cpu_move == "p":
    print("Tie")
elif player_move == "s" and cpu_move == "p":
    print("You win!")
elif player_move == "r" and cpu_move == "s":
    print("You win!")
elif player_move == "p" and cpu_move == "s":
    print("You lose.")
else:
    print("Tie")