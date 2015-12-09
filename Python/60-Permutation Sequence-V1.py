class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        pool = range(1, n+1)
        total = reduce(lambda x,y : x*y, pool)
        result = ''
        k = k - 1
        for i in range(n, 0, -1):
            total = total / i
            index = k / total
            k = k % total
            result += str(pool.pop(index))
        return result
