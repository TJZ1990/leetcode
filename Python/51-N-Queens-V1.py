#backtracking algorithm
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = ['X']*n
        result = []
        self.solve(board, n, 0, result)
        return result
        
    def solve(self, board, n, row, result):
        if row == n:
            result.append(['.'*board[i]+'Q'+'.'*(n-board[i]-1) for i in range(n)])
            return
        
        for col in range(n):
            valid = True
            for i in range(row):
                if col == board[i] or abs(i-row) == abs(board[i]-col):
                    valid = False
                    break
            if valid:
                board[row] = col
                self.solve(board[:], n, row+1, result)
