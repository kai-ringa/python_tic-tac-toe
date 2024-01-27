# Function showing the present state of the board
def print_board(board):
    print(f" {str(board[0]).center(2)}| {str(board[1]).center(2)}| {str(board[2])}")
    print('-----------')
    print(f" {str(board[3]).center(2)}| {str(board[4]).center(2)}| {str(board[5])}")
    print('-----------')
    print(f" {str(board[6]).center(2)}| {str(board[7]).center(2)}| {str(board[8])}")

def check_win(board):
    # Check if there is a winner
    # Check the rows combinations
    for i in range(0, 9, 3):
        if board[i] != '' and board[i] == board[i + 1] == board[i + 2]:
            return True
        
    # Check the columns combinations
    for i in range(3):
        if board[i] != '' and board[i] == board[i + 3] == board[i + 6]:
            return True
        
    # Check the diagonals combinations
    if board[0] != '' and board[0] == board[4] == board[8]:
        return True
    if board[2] != '' and board[2] == board[4] == board[6]:
        return True
    
    return False

def main():
    board = [''] * 9
    is_player1_turn = True # Keep track the player playing
    moves = 0 # Count number of moves made

    print('WELCOME PLAYERS')

    print('GAME START!')

    print_board(board)

    while True:
        print(f'\n{"Player 1" if is_player1_turn else "Player 2"}, enter your move (1 - 9)')

        try:
            move = int(input()) # Read the input from the user

            if move < 1 or move > 9 or board[move - 1] != '':
                # Checking for the validity of the move
                print('Your input is invalid')
                continue

            board[move - 1] = 'X' if is_player1_turn else 'O' # Maintaining the board status
            moves += 1
            print_board(board)

            if check_win(board):
                # Check for winner
                print(f'{"Player 1" if is_player1_turn else "Player 2"} Wins the game')
                break
            elif moves == 9:
                print('GAME DRAW!')
                break

            is_player1_turn = not is_player1_turn

        except ValueError:
            print('Your inputs are invalid, the input should be 1 - 9')

if __name__ == "__main__":
    main()
