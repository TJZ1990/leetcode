#use python's list comprehension
#reference: https://leetcode.com/discuss/42550/one-liners-in-python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n]+p for i,n in enumerate(nums) for p in self.permute(nums[:i]+nums[i+1:])] or [[]]
