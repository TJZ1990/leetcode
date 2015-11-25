#initial version
#traverse the list: calculate left boundary and right boundary each time, and
#if height[i] is smaller than left and right, it can contain water.
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = 0
        result = 0
        for i in range(1, len(height)-1):
            if i >= right:
                right = self.findMax(height, i+1)
                
            bound = min(height[left], height[right])
            if height[i] < bound:
                result += bound - height[i]
                
            if height[i] > height[left]:
                left = i
                
        return result
    
    def findMax(self, height, start):
        maxIndex = start
        maximum = height[start]
        for i in range(start+1, len(height)):
            if height[i] > maximum:
                maximum = height[i]
                maxIndex = i
        return maxIndex
