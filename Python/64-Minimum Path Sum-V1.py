#dynamic programming
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        dp = [grid[0][0]] * n
        for i in range(1, n):
            dp[i] = dp[i-1] + grid[0][i]
        
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        
        return dp[n-1]
