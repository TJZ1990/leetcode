#dynamic programming path[i][j] = path[i-1][j] + path[i][j-1]
#or we can calculate (n+m-2)!/((n-1)!*(m-1)!)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return self.uniquePaths(n, m)
        
        col = [1] * m
        for _ in range(n-1):
            for i in range(1, m):
                col[i] = col[i-1] + col[i]
        
        return col[m-1]
