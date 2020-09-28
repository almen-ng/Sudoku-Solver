# Sudoku Grid
# Edit the Sudoku Board to match the sudoku board you want to solve
# 0 for empty cells, numbers 1-9 for the rest
sudoku_board = [
    [7, 0, 0, 0, 8, 9, 0, 0, 0],
    [0, 0, 1, 2, 0, 0, 0, 0, 0],
    [6, 0, 8, 5, 0, 0, 0, 0, 0],
    [0, 0, 6, 3, 5, 0, 4, 0, 0],
    [0, 8, 0, 9, 0, 7, 0, 3, 0],
    [0, 0, 3, 0, 2, 8, 9, 0, 0],
    [0, 0, 0, 0, 0, 5, 2, 0, 4],
    [0, 0, 0, 0, 0, 3, 1, 0, 0],
    [0, 0, 0, 6, 1, 0, 0, 0, 8]
]

# Utility function display sudoku board in terminal
# Prints a line of - after every 3 rows
# Prints "| " after every 3 columns
def display_sudoku_board(sudoku_board):
    for i in range(len(sudoku_board)):
        if (i % 3 == 0 and i != 0):
            print("-" * 22)
        for j in range(len(sudoku_board)):
            if (j % 3 == 0 and j != 0):
                print(end="| ")
            print(sudoku_board[i][j], end=" ")
        print(" ")
    print(" ")

# Find an empty cell in the sudoku board.
# Return the reference parameters row (i), and column (j)
def empty_cell(sudoku_board):
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board)):
            if(sudoku_board[i][j] == 0):
                return i, j
    return False

# Checking if a number is valid
def is_valid(sudoku_board, number, position):
    # Check each element in the row and see if it matches the given number ignoring if its the position just inserted
    for i in range(len(sudoku_board[0])):
        if(sudoku_board[position[0]][i] == number and position[1] != i):
            return False

    # Check each element in the column and see if it matches the given number ignoring if its the position just inserted
    for i in range(len(sudoku_board)):
        if(sudoku_board[i][position[1]] == number and position[0] != i):
            return False

    # Check each box and see if it matchess the given number ignoring if its the position just inserted
    x = (position[1]//3) * 3
    y = (position[0]//3) * 3

    for i in range(3):
        for j in range(3):
            if(sudoku_board[y+i][x+j] == number and (y+i, j+i) != position):
                return False
    return True

# Takes a partially filled sudoku board and tries to assign values to empty cells meeting requirements of sudoku
def solve(sudoku_board):
    position = empty_cell(sudoku_board)

    # Found solution, return True
    if (position == False):
        return True

    # Loop through values 1-9 in attempt to put those in the solution
    for number in range(1, 10):
        # If valid, put it in the board
        if(is_valid(sudoku_board, number, position)):
            sudoku_board[position[0]][position[1]] = number

            # Recursively try to finish the solution
            if(solve(sudoku_board)):
                return True
            sudoku_board[position[0]][position[1]] = 0

    # None of the numbers iterated so there is no solution
    return False


# Display the initial sudoku board
print("Submitted Sudoku Board:")
display_sudoku_board(sudoku_board)

# If there is a solution, print it; otherwise, tell the user there isn't
if(solve(sudoku_board)):
    print("Solved Sudoku Board:")
    display_sudoku_board(sudoku_board)
else:
    print("No Solution Exists")
