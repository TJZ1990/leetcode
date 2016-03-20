class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
            
        result = [[1]]
        cur = [1]
        for _ in range(1, numRows):
            tmp = [1]
            for i in range(1, len(cur)):
                tmp.append(cur[i] + cur[i-1])
            tmp.append(1)
            cur = tmp
            result.append(cur)
        
        return result