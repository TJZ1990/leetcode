class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.append(0)
        stack = []
        maxArea = 0
        for i in range(len(height)):
            while stack != [] and height[i] < height[stack[-1]]:
                h = height[stack[-1]]
                stack.pop()
                j = stack[-1] if stack != [] else -1
                maxArea = max(maxArea, h*(i-j-1))
            stack.append(i)
        return maxArea
