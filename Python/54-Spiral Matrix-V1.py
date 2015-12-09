#when boundary is reached, change direction. maxStep stores boundary.
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if matrix == []:
            return []
        direction = 0
        m, n = len(matrix), len(matrix[0])
        maxStep = [n, m-1, n-1, m-2]
        step, i, j = 0, 0, -1
        for _ in range(m*n):
            if direction == 0:
                j += 1
            elif direction == 1:
                i += 1
            elif direction == 2:
                j -= 1
            elif direction == 3:
                i -= 1
            step += 1
            result.append(matrix[i][j])
            if step == maxStep[direction]:
                step = 0
                maxStep[direction] -= 2
                direction = (direction + 1) % 4
                
        return result
