class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
            
        i = 2
        for j in range(2, len(nums)):
            if nums[j] > nums[i-2]:
                nums[i] = nums[j]
                i += 1

        return i