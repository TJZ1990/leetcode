class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [0]*(len(t)+1)
        dp[0] = 1
        
        for i in range(1, len(s)+1):
            pre = 1
            for j in range(1, len(t)+1):
                tmp = dp[j]
                if s[i-1] == t[j-1]:
                    dp[j] += pre
                pre = tmp
        return dp[len(t)]
