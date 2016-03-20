class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        
        row = [1]
        for _ in range(rowIndex):
            for i in reversed(range(1, len(row))):
                row[i] += row[i-1]
            row.append(1)
        return row