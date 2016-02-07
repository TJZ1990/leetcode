#fibonacci
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        a = 1
        b = 1
        for _ in range(n):
            a, b = b, a+b
        return a
