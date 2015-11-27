#use a set to avoid duplication
class Solution(object):
    def permuteUnique(self, nums):
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
        
        numSet = set()
        for i in range(start, len(nums)):
            if nums[i] in numSet:
                continue
            else:
                numSet.add(nums[i])
            nums[start], nums[i] = nums[i], nums[start]
            self.calPermutation(nums[:], start+1)
            nums[start], nums[i] = nums[i], nums[start]
