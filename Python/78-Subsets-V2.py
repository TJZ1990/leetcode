# bit manipulation
# There are 2^n subsets.
# For example, nums = [1, 2, 3], the fifth(binary: 101) subset means it cotains 1 and 3, so it's [1, 3].
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = pow(2, len(nums))
        result = [[] for _ in range(l)]
        
        for i in range(len(nums)):
            for j in range(l):
                if (j >> i) & 1:
                    result[j].append(nums[i])
        return result
