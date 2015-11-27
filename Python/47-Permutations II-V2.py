#use the algorithm in next permutation
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [nums[:]]
        
        while True:
            i = len(nums) - 1
            while i > 0:
                if nums[i] > nums[i-1]:
                    break
                i -= 1
            else:
                return result
            
            nums[i:] = reversed(nums[i:])
            j = i
            while j < len(nums) and nums[i-1] >= nums[j]:
                j += 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
            result.append(nums[:])
