#finds the next row and col on the puzzle that is empty
def findNextEmpty(puzzle):
    #define any open spaces with -1
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None    #return row, col tuple or (None, None) if the board is full: no empty spaces

def solveSudoku(puzzle):
    #mutates puzzle to be the solution if a solution exists

    #1. choose where to make the first guess
    row, col = findNextEmpty(puzzle)
    if row is None:
        return True