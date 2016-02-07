class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.calSubsets(nums, 0, [], result)
        return result
    
    def calSubsets(self, nums, start, cur, result):
        if start == len(nums):
            result.append(cur)
            return
        
        self.calSubsets(nums, start+1, cur, result)
        self.calSubsets(nums, start+1, cur+[nums[start]], result)
