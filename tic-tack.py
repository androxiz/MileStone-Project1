import random

#Decides what player should go first
def first_turn():
    random_number = random.randint(1, 2)
    print(f"Player {random_number} goes first!")
    return random_number

#Clears the console
def clear_console():
    print("\n"*100)

#Displays the playing board
def display_board(board):
    clear_console()

    print(board[6], "|", board[7], "|", board[8])
    print("--|---|--")
    print(board[3], "|", board[4], "|", board[5])
    print("--|---|--")
    print(board[0], "|", board[1], "|", board[2])

#Allows to choose the team
def choose_team():
    marker = ""

    while marker != "X" and marker != "O":
        marker = input("Player 1, choose your team (X or O): ").upper()
        if marker != "X" and marker != "O":
            clear_console()
            print("Incorrect choise! Choose the correct team")

    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)


#Checks if the user`s position is empty
def is_empty_position(board, position):
    return board[position] == " "

#Checks if the board is full
def is_full(board):
    return " " not in board


#Gives an opportunity to start game again
def replay():
    answer = "Wrong"

    while answer != "y" and answer != "n":
        answer = input("Do u want to continue? Select Y or N: ").lower()

        if answer != "y" and answer != "n":
            clear_console()
            print("Incorrect answer!")
    if answer == "y":
        return True
    else:
        return False


#Asks a position to put a mark
def choose_position(board):  #position =
    position = "Wrong"
    is_in_range = False
    is_space_free = False

    while position.isdigit() == False or is_in_range == False or is_space_free == False:
        position = input("Please, select a position (1 - 9): ")
        
        if position.isdigit() == False:
            clear_console()
            display_board(board)
            print("Incorrect value! It must be a digit!")
        
        if position.isdigit():
            if int(position) - 1 in range(0, 9):
                is_in_range = True
            else:
                clear_console()
                display_board(board)
                print("The value must be from 1 to 9!")
        if position.isdigit() and int(position) - 1 in range(0, 9):
            if is_empty_position(board, int(position) - 1):
                is_space_free = True
            else:
                clear_console()
                display_board(board)
                print("This spot is busy!")
    
    position = int(position)
    return position - 1
    

#Change a board depends on its position
def change_board(board, position, mark):
    board[position] = mark

def ask_for_ready():
    answer = "Wrong"
    while answer != "yes" and answer != "no":
        answer = input("Are u ready to start? \n").lower()

        if answer != "yes" and answer != "no":
            clear_console()
            print("Incorrect answer!")

    return answer

#Check if there is a win combination or not
def win_check(board, mark):
    if board[6] == board[7] == board[8] == mark:
        return True
    elif board[3] == board[4] == board[5] == mark:
        return True
    elif board[0] == board[1] == board[2] == mark:
        return True
    elif board[6] == board[3] == board[0] == mark:
        return True
    elif board[7] == board[4] == board[1] == mark:
        return True
    elif board[8] == board[5] == board[2] == mark:
        return True
    elif board[6] == board[4] == board[2] == mark:
        return True
    elif board[0] == board[4] == board[8] == mark:
        return True
    else:
        return False


def start_game():
    print('Welcome to my first game made on Python, which is called "Tic-Tac".')

    is_replay = True
    while is_replay:
        board = [" "] * 9
        p1_marker, p2_marker = choose_team()
        turn = first_turn()

        answer = ask_for_ready()

        if answer == "yes":
            pass
        else:
            break

        while True:
            if is_full(board):
                clear_console()
                print("Tie!")
                break

            if turn == 1:
                display_board(board)
                print(f"First player's turn! Your mark is: {p1_marker}")
                position = choose_position(board)
                change_board(board, position, p1_marker)
                if win_check(board, p1_marker):
                    display_board(board)
                    print("Player 1 has won!")
                    break
                turn = 2

            if turn == 2:
                display_board(board)
                print(f"Second player's turn! Your mark is: {p2_marker}")
                position = choose_position(board)
                change_board(board, position, p2_marker)
                if win_check(board, p2_marker):
                    display_board(board)
                    print("Player 2 has won!")
                    break
                turn = 1

        is_replay = replay()
        clear_console()


if __name__ == "__main__":
    start_game()