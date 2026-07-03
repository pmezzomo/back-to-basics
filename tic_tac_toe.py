board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

player = 'X'

def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def make_move(row, col):
    if (
        not 0 <= row <= 2 or
        not 0 <= col <= 2 or
        board[row][col] != ' '
    ):
        print('Invalid move!')
        return player
    board[row][col] = player
    return 'O' if player == 'X' else 'X'

def has_winner():
    # Check rows
    for row in range(3):
        if (
            board[row][0] != ' ' and
            board[row][0] == board[row][1] and
            board[row][0] == board[row][2]
        ):
            print(f'{board[row][0]} WON!!!')
            return True

    # Check columns
    for col in range(3):
        if (
            board[0][col] != ' ' and
            board[0][col] == board[1][col] and
            board[0][col] == board[2][col]
        ):
            print(f'{board[0][col]} WON!!!')
            return True

    # Check diagonals
    if (
        board[1][1] != ' ' and
        (
            (
                board[0][0] == board[1][1] and
                board[0][0] == board[2][2]
            ) or
            (
                board[0][2] == board[1][1] and
                board[1][1] == board[2][0]
            )
        )
    ):
        print(f'{board[1][1]} WON!!!')
        return True

    # No winner found
    return False

def is_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    print("It's a draw!")
    return True

while True:
    print(f"Player's turn: {player}")
    try:
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
        player = make_move(row, col)
    except (IndexError, ValueError):
        print('Enter numeric values between 0 and 2!')
    display_board()
    if has_winner() or is_draw():
        break
