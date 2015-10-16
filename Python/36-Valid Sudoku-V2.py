class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        #O(n^2) method
        
        setRow = []
        setColumn = []
        setSub = []
        for i in range(9):
            setRow.append([0]*9)
            setColumn.append([0]*9)
            setSub.append([0]*9)

        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    continue
                n = int(board[row][column]) - 1 
                if setRow[row][n] or setColumn[column][n] or setSub[row/3*3+column/3][n]:
                    return False
                else:
                    setRow[row][n] = setColumn[column][n] = setSub[row/3*3+column/3][n] = 1

        return True
