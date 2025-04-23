import random   # for computer move

board = [[" " for row in range(3)] for column in range(3)]  # initializing 3x3 matrix to board

# welcome message
def welcome():
    print("\nWelcome to Tic Tac Toe!")
    print("\nThis is the corresponding move number on the board:\n")

# assign square numbers as initial values to board
def move_number():
    num = 1
    for row in range(3):
        for column in range(3):
            board[row][column] = num
            num += 1

# printing the board
def print_board():
    for row in board:
        print(("+" + "-" * 7) * 3, end="+\n")
        print(("|" + " " * 7) * 3, end="|\n")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print(("|" + " " * 7) * 3, end="|\n")
    print(("+" + "-" * 7) * 3, end="+\n")

# checks if move is valid
def check_valid_move(move):
    if board[move[0]][move[1]] == 'X' or board[move[0]][move[1]] == 'O':
        return False
    return True

# checking if there is a winner
def check_winner():
    winning_patterns = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]

    for elem in winning_patterns:
        if elem[0] and elem[0] == elem[1] and elem[1] == elem[2] and elem[2] == elem[0]:
            return True
    return False

# dictionary for moves
moves_dictionary = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2)
}

### Game ###
welcome()  # invoking the welcome() function
move_number()  # assigning move number as initial values on the board
board[1][1] = 'X'  # Computer always moves first at the center
print_board()  # print current board

move_turn = 1  # to determine whose turn

# Game loop
while True:
    is_move_valid = False  # setting initial value as False
    if move_turn % 2 == 0:
        # computer moves
        while not is_move_valid:  # while computer move is invalid,
            # computer picks random move
            computer_input = random.randint(1, 9) # random move
            computer_move = moves_dictionary[computer_input]
            if check_valid_move(computer_move):  # if computer move is valid,
                is_move_valid = True  #  set is_move_valid to true to exit while loop
                board[computer_move[0]][computer_move[1]] = 'X'
    else:
        # user moves
        while not is_move_valid:  # while user move is invalid,
            user_input = int(input("Enter your move: "))
            if user_input in moves_dictionary:  # check if user_input is in dictionary (1-9)
                user_move = moves_dictionary[user_input]
                if check_valid_move(user_move):  # if user move is valid,
                    is_move_valid = True  # set is_move_valid to true to exit while loop
                    board[user_move[0]][user_move[1]] = 'O'
            # else: re-loop

    # print current board
    print_board()

    # checking if there is a winner
    if check_winner():
        if move_turn % 2 == 0:
            print("\nComputer won!")
        else:
            print("\nYou won!")
        break  # exit the game loop
    elif move_turn == 8:  # if no winner after move 8
        print("\nThe game is draw!")
        break  # exit the game loop

    move_turn += 1  # increment move_turn to change turns


