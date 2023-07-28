WordsearchGrid = "hellor\n" + "asdnja\n" + "odlrow\n" + "yesabc\n" + "oyuanx\n"

Words = ["hello", "world", "yes", "no"]

def ColumntoRow(Grid):
    """
    Transposes columns to rows for a 1d list containing strings, 
    """
    outlist = ["" for i in Grid[0]]
    for Row in range(len(Grid)):
        for Column in range(len(Grid[Row])):
            outlist[Column]+=(Grid[Row][Column])#swapping rows for columns by inverting indexes
    return outlist

def Diagonalise(Grid):
    """Diagonalises the given grid
    Could have compacted all the for loops, but thought I may as well leave it explicit"""
    OutList = ["" for i in range(2*(len(Grid) + len(Grid[0])-1))]
    for RowGrid in range(len(Grid)): #diagonalising starting at left column, down and right
        Column = 0
        Row = RowGrid
        while Row < len(Grid) and Column < len(Grid[0]):
            OutList[RowGrid] += Grid[Row][Column]
            Row += 1
            Column += 1
    for ColumnGrid in range(len(Grid[0][1:])): #diagonalising starting at top row, down and right
        Row = 0
        Column = ColumnGrid+1
        while Row < len(Grid) and Column < len(Grid[0]):
            OutList[ColumnGrid+len(Grid)] += Grid[Row][Column]
            Row += 1
            Column += 1
    for RowGrid in range(len(Grid)): #diagonalising starting at right column, down and left
        Column = len(Grid[0])-1
        Row = RowGrid
        while Row < len(Grid) and Column >= 0:
            OutList[RowGrid+len(Grid)+len(Grid[0])-1] += Grid[Row][Column]
            Row += 1
            Column -= 1
    for ColumnGrid in range(len(Grid[0][1:])): #diagonalising starting at top row, down and left
        Row = 0
        Column = ColumnGrid + 1
        while Row < len(Grid) and Column >= 0:
            OutList[ColumnGrid+2*len(Grid)+len(Grid[0])-1] += Grid[Row][Column]
            Row += 1
            Column -= 1
    return OutList

def WordSearch(Grid, Words):
    """
    Checks if a list of words is contained within a wordsearch grid: 
    Horisontal forwards and reverse only
    """
    ReturnList = [] #empty list to store detected words
    Grid = Grid.split("\n")[:-1] #removing line breaks

    Directions = []
    Directions += Grid + ColumntoRow(Grid) + Diagonalise(Grid)

    for Direction in Directions:
        for ForwardReverse in (Direction, Direction[::-1]): #forward and reverse directions for each direction
            for Word in Words:
                if Word in ForwardReverse:
                    ReturnList.append(Word)
    return ReturnList

print(WordSearch(WordsearchGrid, Words))
