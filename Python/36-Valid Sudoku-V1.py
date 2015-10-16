class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        numberSet = set()
        #check each row
        for row in board:
            numberSet.clear()
            for number in row:
                if number == '.':
                    continue
                if number in numberSet:
                    return False
                else:
                    numberSet.add(number)
        
        #check each column
        for column in range(9):
            numberSet.clear()
            for row in range(9):
                number = board[row][column]
                if number == '.':
                    continue
                if number in numberSet:
                    return False
                else:
                    numberSet.add(number)
        
        #check each sub-box
        for i in range(3):
            for j in range(3):
                numberSet.clear()
                for m in range(3):
                    for n in range(3):
                        number = board[i*3+m][j*3+n]
                        if number == '.':
                            continue
                        if number in numberSet:
                            return False
                        else:
                            numberSet.add(number)
        
        return True  
