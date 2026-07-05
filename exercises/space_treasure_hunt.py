"""
Space Treasure Hunt
A treasure is hidden on a 3x3 map. You have 5 chances to find it!
"""

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

treasure_row = 1
treasure_col = 2

def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

print("🚀 Welcome to Space Treasure Hunt!")
print("A treasure 💎 is hidden somewhere on this 3x3 map.")
print("You have 5 attempts. Rows and columns go from 0 to 2.\n")
display_board()

for attempt in range(1, 6):
    print(f"\nAttempt {attempt} of 5")
    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
    except ValueError:
        print("⚠️ Please enter valid numbers!")
        continue

    if not (0 <= row <= 2 and 0 <= col <= 2):
        print("⚠️ Invalid position! Row and column must be between 0 and 2.")
        continue

    if board[row][col] != ' ':
        print("⚠️ You already tried that spot!")
        continue

    if row == treasure_row and col == treasure_col:
        board[row][col] = '💎'
        display_board()
        print(f"\n🎉 You found the treasure in {attempt} attempt(s)!")
        break
    else:
        board[row][col] = 'X'
        display_board()
        print("❌ Nothing here. Keep searching!")
else:
    print(f"\n💀 Game over! The treasure was at row {treasure_row}, column {treasure_col}.")
