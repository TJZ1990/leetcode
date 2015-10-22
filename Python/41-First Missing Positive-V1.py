#initial version
#time: O(nlogn) space: O(n)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        for i in range(len(nums)):
            if nums[i] > 0:
                break
        else:
            return 1
            
        for j in range(i, len(nums)):
            if nums[j] != j - i + 1:
                return j - i + 1
        return j+1-i+1
