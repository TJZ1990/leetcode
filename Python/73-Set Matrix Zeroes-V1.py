#Use the first row and the first column to mark whether this row/column should be 0.
#matrix[0][0] represents the 1st row and the 1st column, so we use col0.
#O(1) space, O(m*n) time
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        col0 = 1
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    print i,j
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in reversed(range(m)):
            for j in reversed(range(1, n)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
