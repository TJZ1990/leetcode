#A L-length nums's largest missing positive integer is L+1
#So we can use a method like bitmap search. nums[0] stores 1, nums[1] stores 2...
#time: O(n) space: O(1)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i]-1 != i and nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums)+1
