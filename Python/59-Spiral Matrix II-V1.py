#modified from Spiral Matrix
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for _ in range(n)]
        direction = 0
        maxStep = [n, n-1, n-1, n-2]
        step, i, j = 0, 0, -1
        for count in range(1, n*n+1):
            if direction == 0:
                j += 1
            elif direction == 1:
                i += 1
            elif direction == 2:
                j -= 1
            elif direction == 3:
                i -= 1
            step += 1
            matrix[i][j] = count
            if step == maxStep[direction]:
                step = 0
                maxStep[direction] -= 2
                direction = (direction + 1) % 4
                
        return matrix
