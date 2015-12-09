class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        col = [0] * m
        
        #initialize first column
        for i in range(m):
            if obstacleGrid[i][0]:
                break
            col[i] = 1
            
        for i in range(1, n):
            if obstacleGrid[0][i]:
                col[0] = 0
            for j in range(1, m):
                col[j] = 0 if obstacleGrid[j][i] else (col[j] + col[j-1])

        return col[m-1]
