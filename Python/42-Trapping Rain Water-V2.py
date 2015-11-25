#improved version
#use two pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height)-1
        leftMax = 0
        rightMax = 0
        result = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] < leftMax:
                    result += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    result += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return result
