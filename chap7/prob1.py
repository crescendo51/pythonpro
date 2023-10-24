def instructions() :
    # A function that explains the game
    print("\tWelcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.")
    print("\tThis will be a showdown between your human brain and my silicon processor.")
    print('')
    print("\tYou will make your move known by entering a number, 0 - 8. The number will correspond to the board position as illustrated:")
    print("")

def ask_yes_no() :
    answer = input("Do you require the first move? (y/n): ")
    return answer

def player_turn() :
    get_num = int(input("Where will you move? (0-8): "))
    print("Fine..")
    if board[get_num] != 'X' and board[get_num] != 'O':
        board[get_num] = 'X'
        print('')
        draw_board()
        print('')
        if check_winner('X'):
            print("X won!")
            print('')
            print("No, no! It cannot be! Somehow you tricked me, human.")
            print("But never again! I, the computer, so swears it!")
            print('')
            return True
        if check_draw():
            print("It's a draw!")
            return True
    else:
        print("Invalid move. Try again.")
        player_turn()

def computer_turn() :
    import random
    while True:
        get_num = random.randint(0, 8)
        if board[get_num] != 'X' and board[get_num] != 'O':
            board[get_num] = 'O'
            print("I shell take square number %d" %get_num)
            print('')
            draw_board()
            print('')
            
            if check_winner('O'):
                print("O won!")
                print('')
                print("As I predicted, human, I am triumphant once more.")
                print("Proof that computers are superior to humans in all regards.")
                return True
            if check_draw():
                print("It's a draw!")
                return True
            break

def draw_board() :
    print("\t%s | %s | %s" %(board[0],board[1],board[2]))
    print("\t---------")
    print("\t%s | %s | %s" %(board[3],board[4],board[5]))
    print("\t---------")
    print("\t%s | %s | %s" %(board[6],board[7],board[8]))

def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw():
    return all(cell == 'X' or cell == 'O' for cell in board)

instructions()
board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
draw_board()
print('')
print("\tPrepare yourself, huma. The ultimate battle is about to begin.\n")
choice = ask_yes_no()

def turn(choice) :
    if choice == 'y' :
        print("Okay. You go first.")
        while True:
            if player_turn():
                break
            if computer_turn():
                break
    elif choice == 'n' :
        print("Okay. I'll go first.")
        while True:
            if computer_turn():
                break
            if player_turn():
                break

turn(choice)
