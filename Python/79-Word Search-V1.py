class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if self.check(board, word, 0, i, j, m, n):
                    return True
        return False
    
    def check(self, board, word, pos, i, j, m, n):
        #print i,j,pos,board[i][j]
        if pos == len(word):
            return True
        
        if i < 0 or i >= m or j < 0 or j >=n:
            return False
        
        if board[i][j] != word[pos]:
            return False
        
        bakup = board[i][j]
        board[i][j] = '*'
        res = False
        for x,y in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if self.check(board, word, pos+1, x, y, m, n):
                res = True
                break
        board[i][j] = bakup
        return res
        
        
        
