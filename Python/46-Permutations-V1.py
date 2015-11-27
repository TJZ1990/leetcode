#backtracking algorithm
#In this problem, every element in nums is treated as a unique one.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.calPermutation(nums, 0)
        return self.result
    
    def calPermutation(self, nums, start):
        if start == len(nums):
            self.result.append(nums)
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.calPermutation(nums[:], start+1)
            nums[start], nums[i] = nums[i], nums[start]
