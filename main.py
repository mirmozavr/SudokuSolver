board = [[5, 0, 9, 0, 0, 3, 0, 0, 4],
         [0, 0, 0, 1, 0, 0, 3, 6, 2],
         [6, 0, 0, 0, 2, 0, 0, 0, 0],
         [0, 7, 0, 0, 4, 0, 2, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 4, 0],
         [0, 0, 4, 0, 5, 0, 0, 8, 0],
         [0, 0, 0, 0, 8, 0, 0, 0, 6],
         [9, 5, 3, 0, 0, 2, 0, 0, 0],
         [8, 0, 0, 5, 0, 0, 7, 0, 3]]


def enter_sudoku():
    b = []
    for z in range(9):
        b.append(list(map(int,input("Enter one line (example: 300400610) "))))
    return b


def board_print(b):
    for i in range(9):
        if not i % 3 and i != 0:
            print("- " * 10 + '-')
        for j in range(9):
            if not j % 3 and j not in (0, 8):
                print("| ", end='')
            print(b[i][j], end=(' ' if j != 8 else ''))
        print()


def find_empty_field(b):
    for i in range(9):
        for j in range(9):
            if not b[i][j]:
                return i, j
    return None, None


def valid(b, num, row, col):  # validity of given num in given row and col on board
    # check row
    for j in range(9):
        if b[row][j] == num:
            return False
    # check column
    for i in range(9):
        if b[i][col] == num:
            return False
    # check square
    for i in range((row // 3) * 3, (row // 3 + 1) * 3):
        for j in range((col // 3) * 3, (col // 3 + 1) * 3):
            if b[i][j] == num:
                return False
    return True


def solve(b):
    row, col = find_empty_field(b)
    if (row, col) == (None, None):
        return True
    for x in range(1, 10):
        if valid(b, x, row, col):
            b[row][col] = x
            if solve(b):
                return True
            b[row][col] = 0
    return False


ans = input('Enter your sudoku? yes or no : ')
if ans == 'yes':
    board = enter_sudoku()

print('Original')
board_print(board)
print('__' * 16)
print('Solved')
solve(board)
board_print(board)
