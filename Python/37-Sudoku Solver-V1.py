#backtracking
#use three sets to check if a number is valid
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        setRow = [set() for _ in range(9)]
        setCol = [set() for _ in range(9)]
        setSub = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    setRow[r].add(board[r][c])
                    setCol[c].add(board[r][c])
                    setSub[r//3*3+c//3].add(board[r][c])
        self.solve(board, 0, 0, setRow, setCol, setSub)
        
    def solve(self, board, r, c, setRow, setCol, setSub):
        if board[r][c] != '.':
            if r == 8 and c == 8:
                return True
            else:
                return self.solve(board, r+(c+1)//9, (c+1)%9, setRow, setCol, setSub)
        else:
            for number in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if (number not in setRow[r]) and (number not in setCol[c]) and (number not in setSub[r//3*3+c//3]):
                    setRow[r].add(number)
                    setCol[c].add(number)
                    setSub[r//3*3+c//3].add(number)
                    board[r][c] = number
                    if r == 8 and c == 8:
                        return True
                    elif self.solve(board, r+(c+1)//9, (c+1)%9, setRow, setCol, setSub):
                        return True
                    
                    setRow[r].remove(number)
                    setCol[c].remove(number)
                    setSub[r//3*3+c//3].remove(number)
                    board[r][c] = '.'
            return False
                
                    
      
