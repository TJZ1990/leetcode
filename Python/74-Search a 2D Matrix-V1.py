#Treat the matrix as array.
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = m*n - 1
        while l <= r:
            mid = l + (r-l)/2
            if matrix[mid/n][mid%n] == target:
                return True
            elif matrix[mid/n][mid%n] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        
        
        
        
        
