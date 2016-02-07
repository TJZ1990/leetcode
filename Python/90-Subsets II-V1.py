class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.calSubset(nums, 0, [], result)
        return result
    
    def calSubset(self, nums, start, cur, result):
        result.append(cur)
        
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i-1]:
                self.calSubset(nums, i+1, cur+[nums[i]], result)
