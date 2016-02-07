class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None or matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        row = [0] * n
        
        maxRec = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    row[j] += 1
                else:
                    row[j] = 0
            maxRec = max(maxRec, self.findMaxRect(row))
        
        return maxRec
        
    def findMaxRect(self, height):
        maxArea = 0
        stack = []
        for i in range(len(height)+1):
            cur = height[i] if i < len(height) else 0
            while stack != [] and cur < height[stack[-1]]:
                h = height[stack[-1]]
                stack.pop()
                j = stack[-1] if stack != [] else -1
                maxArea = max(maxArea, h*(i-j-1))
            stack.append(i)
            
        return maxArea
        
        
        
        
        
        
        
