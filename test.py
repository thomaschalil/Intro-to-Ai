import random

def print_board(board):
    print("+" + "-" * 11 + "+") 
    for row in board:
        print("| " + " | ".join(row)+ " |")
        print("|" + "-" * 11 + "|") 
        
def print_board_init(board):
    print("+" + "-" * 11 + "+") 
    for temp in range(0,3):
        print("| " + str(3*temp) + " | " + str(3*temp+1) + " | " + str(3*temp+2) + " |")
        if temp == 2:
        	print("+" + "-" * 11 + "+") 
        else:
            print("|" + "-" * 11 + "|")


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']

def optimal(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'tie': 0}
    
    if check_winner(board, 'X'):
        return scores['X']
    if check_winner(board, 'O'):
        return scores['O']
    if check_full(board):
        return scores['tie']

    if is_maximizing:
        max_eval = float('-inf')
        for row, col in get_empty_cells(board):
            board[row][col] = 'O'
            eval = optimal(board, depth + 1, False)
            board[row][col] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in get_empty_cells(board):
            board[row][col] = 'X'
            eval = optimal(board, depth + 1, True)
            board[row][col] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_score = float('-inf')
    best_move = (-1, -1)
    for row, col in get_empty_cells(board):
        board[row][col] = 'O'
        score = optimal(board, 0, False)
        board[row][col] = ' '
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

def play_tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        player_turn = True
        init = True

        while True:
            if init:
                print_board_init(board)
                init = False
            else:
                print_board(board)
            if player_turn:
                move = input("Enter your move (0-8): ")
                if not move.isdigit() or not (0 <= int(move) <= 8):
                    print("Invalid input. Please enter a number from 0 to 8.")
                    continue
                move = int(move)
                row, col = divmod(move, 3)
            else:
                print("Computer's turn...")
                row, col = best_move(board)

            if board[row][col] == ' ':
                board[row][col] = 'X' if player_turn else 'O'
                if check_winner(board, 'X' if player_turn else 'O'):
                    print_board(board)
                    print("Congratulations! " + ("You" if player_turn else "Computer") + " won!")
                    break
                elif check_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                player_turn = not player_turn
            else:
                print("That spot is already taken. Try again.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes' and play_again.lower() != "y":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
