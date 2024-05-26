#finds the next row and col on the puzzle that is empty
def findNextEmpty(puzzle):
    #define any open spaces with -1
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None    #return row, col tuple or (None, None) if the board is full: no empty spaces

def isValid(puzzle, guess, row, col):

    rowValues = puzzle[row] 
    if guess in rowValues:
        return False
    
    colvalues = []
    for i in range(9):
        colvalues.append(puzzle[i][col])
    return True

def solveSudoku(puzzle):
    #mutates puzzle to be the solution if a solution exists

    #1. choose where to make the first guess
    row, col = findNextEmpty(puzzle)
    if row is None:
        return True
    
    #2. Make a guess b/w 1 and 9
    for guess in range(1, 10):
        #3: check if this is a valid guess
        if (isValid(puzzle, guess, row, col)):
