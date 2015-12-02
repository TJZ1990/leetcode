#use flagCol, flag45, flag135 to store column and diagonal conflictions 
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = ['X']*n
        result = []
        self.solve(board, n, 0, result, [0]*n, [0]*(2*n-1), [0]*(2*n-1))
        return result
        
    def solve(self, board, n, row, result, flagCol, flag45, flag135):
        if row == n:
            result.append(['.'*board[i]+'Q'+'.'*(n-board[i]-1) for i in range(n)])
            return
        
        for col in range(n):
            if flagCol[col] or flag45[row+col] or flag135[row+n-1-col]:
                continue
            board[row] = col
            flagCol[col] = flag45[row+col] = flag135[row+n-1-col] = 1
            self.solve(board, n, row+1, result, flagCol, flag45, flag135)
            flagCol[col] = flag45[row+col] = flag135[row+n-1-col] = 0
