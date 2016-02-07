class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        pool = range(1, n+1)
        self.calCombine(pool, k, 0, [], result)
        return result
    
    def calCombine(self, pool, length, start, cur, result):
        if len(cur) == length:
            result.append(cur)
            return
        
        for i in range(start, len(pool)):
            self.calCombine(pool, length, i+1, cur+[pool[i]], result)
