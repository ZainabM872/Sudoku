#finds the next row and col on the puzzle that is empty
def findNextEmpty(puzzle):
    #define any open spaces with -1
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None    #return row, col tuple or (None, None) if the board is full: no empty spaces

def isValid(puzzle, guess, row, col):

    rowValues = puzzle[row] #gets the values in the specifies row
    if guess in rowValues:
        return False
    
    colvalues = []
    for i in range(9): #iterates thru each row
        colvalues.append(puzzle[i][col]) #adds the value at column call to list
    if guess in colvalues:
        return False
    
    #the square matrix:

    #find top left corner of grid
    rowStart = (row //3) *3 #finds which of the 3 subgrids the row and columsn r in
    #*3 gives it the starting index of the sub grid
    colStart = (col //3) *3

    for r in range(rowStart, rowStart+3):
        for c in range(colStart, colStart+3):
            if puzzle[r][c] == guess:
                return False
            
    return True #valid guess

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
