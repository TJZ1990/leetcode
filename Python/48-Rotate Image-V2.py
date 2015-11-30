#the rotate equation is i'=j, j'=n-1-i
#four numbers is a cycle, and you only need to deal with a quater of the matrix
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        bound = n/2 if n%2 == 0 else n/2+1
        for i in range(n/2):
            for j in range(bound):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
