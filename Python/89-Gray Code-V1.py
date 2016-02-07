class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return [0]
            
        result = self.grayCode(n-1)
        for i in reversed(range(pow(2, n-1))):
            result.append((1<<(n-1)) + result[i])
        return result
