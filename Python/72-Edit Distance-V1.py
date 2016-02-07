#dynamic programming
#see this https://leetcode.com/discuss/10426/my-o-mn-time-and-o-n-space-solution-using-dp-with-explanation
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = range(len(word2)+1)
        for i in range(1, len(word1)+1):
            dp[0] = i
            pre = i - 1
            for j in range(1, len(word2)+1):
                cur = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j-1], dp[j], pre) + 1
                pre = cur
        return dp[len(word2)]
