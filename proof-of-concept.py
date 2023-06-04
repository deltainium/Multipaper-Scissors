# Winner determination algorithm courtesy of Christopher Shroba on Stackoverflow
# Miles better than a dictionary or several if statements
def winner(p1, p2):
    if (p1+1) % 3 == p2:
        return "\nPlayer 2 wins\n"
    elif p1 == p2:
        return "\nIt's a draw\n"
    else:
        return "\nPlayer 1 wins\n"

def playerselect(num):
    while True:
        select = str(input(f"Player {num} Please choose your move (Rock, Paper, or Scissors): "))
        if select not in moveset:
            print("You have selected a nonexistent move. Remember the move must be capitalised")
            continue
        else:
            select = moveset[select]
            return(select)

def game():
    while True:
        p1 = playerselect(1)
        p2 = playerselect(2)
        print(winner(p1, p2))
        end()

def end():
    while True:
        replay = str(input("Would you like to play again? (y/n): "))
        if replay not in ["y","n"]:
            print("You have made an invalid selection. Please try again")
            continue
        elif replay == "y":
            game()
        else:
            print("Thank you for playing! :)")
            exit()


# Players will be prompted for a move as a string for user friendliness
# The moveset dictionary will be used used to convert
moveset = {
        "Rock":int(0),
        "Paper":int(1),
        "Scissors":int(2),
        }

game()

# Workflow --> Forever p1 chooses an input, p2 chooses an input, winner is calculated and printed, repeat
