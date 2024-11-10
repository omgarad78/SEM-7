def print_board(board, n):
    print("\nCurrent Board Configuration:")
    for i in range(n):
        row = ""
        for j in range(n):
            row += "Q " if board[i][j] == 1 else ". "
        print(row)
    print()

def is_safe(board, row, col, n):
    for j in range(n):
        if board[row][j] == 1:
            return False
    for i in range(n):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def n_queens_interactive():
    n = int(input("Enter board size (4 or greater): "))
    if n < 4:
        print("Board size must be 4 or greater!")
        return

    row, col = int(input("First queen row: ")), int(input("First queen column: "))
    board = [[0] * n for _ in range(n)]
    board[row][col] = 1

    print("\nInitial board with first queen:")
    print_board(board, n)

    # Removed the "Solving..." message and solution handling block as per your request
    if solve_n_queens(board, 0, n):
        print_board(board, n)

# Run interactive function
n_queens_interactive()
