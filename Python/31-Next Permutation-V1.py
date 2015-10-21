#Non-ascending order is the largetst order.
#To get the next permutation, we need to search from the end.
#If the sub-array is in non-ascending order, it's impossible to make it bigger.
#So we need to find a first number from the end which is smaller than its latter one.
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(1, len(nums))):
            if nums[i] > nums[i-1]:
                nums[i:] = nums[:i-1:-1]
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[i-1],nums[j] = nums[j],nums[i-1]
                        return
        nums.reverse()
