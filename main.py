board = [[5, 0, 9, 0, 0, 3, 0, 0, 4],
         [0, 0, 0, 1, 0, 0, 3, 6, 2],
         [6, 0, 0, 0, 2, 0, 0, 0, 0],
         [0, 7, 0, 0, 4, 0, 2, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 4, 0],
         [0, 0, 4, 0, 5, 0, 0, 8, 0],
         [0, 0, 0, 0, 8, 0, 0, 0, 6],
         [9, 5, 3, 0, 0, 2, 0, 0, 0],
         [8, 0, 0, 5, 0, 0, 7, 0, 3]]


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
            solve(b)
            if find_empty_field(b) == (None, None):
                print('\nFound')
                board_print(b)
                global solutions
                solutions += 1
                resp = input("Need more? (type 'no' to quit): ")
                if resp == 'no':
                    quit()
                b[row][col] = 0
                return
            b[row][col] = 0
    return False


solutions = 0
print('Original')
board_print(board)
print('\n'+'#' * 24)
solve(board)
print('\nSolutions:', solutions)
