#curSum means the largest sum ends in current position
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            curSum = nums[i] if curSum < 0 else (curSum+nums[i])
            maxSum = max(curSum, maxSum)
        return maxSum

