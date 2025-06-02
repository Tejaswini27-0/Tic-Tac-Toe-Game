import random

def print_board(board):
    print("\n  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")
    print()

def check_win(board, player):
    # Rows, columns, diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[r][col] == player for r in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_player_move(board):
    while True:
        try:
            move = input("Enter your move (row and column separated by space): ")
            row, col = map(int, move.split())
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Cell occupied or out of range.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")

def get_ai_move(board):
    # Simple AI: random available cell
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells)

def play_game(single_player=False):
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print_board(board)

    while True:
        if single_player and current_player == 1:
            print("AI is making a move...")
            row, col = get_ai_move(board)
        else:
            print(f"Player {players[current_player]}'s turn.")
            row, col = get_player_move(board)

        board[row][col] = players[current_player]
        print_board(board)

        if check_win(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player

def main():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        mode = input("Select mode:\n1. Single Player (vs AI)\n2. Two Players\nEnter choice (1 or 2): ")
        if mode == '1':
            play_game(single_player=True)
        elif mode == '2':
            play_game(single_player=False)
        else:
            print("Invalid choice.")
            continue

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__== "__main__":
    main()