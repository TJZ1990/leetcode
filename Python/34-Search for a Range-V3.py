#version 3
#We can use a trick to simplify the code of version 2.
#To modify searchLeft that it will return an index.
#This index is the first target index or the index of first number bigger than target or the last
#number index(when all numbers are smaller than target).
#
#Then we can use searchLeft(nums, target+1, left, j) to find the first number bigger than target.
# The return index minus 1 is just the right boundary we want.
#Pay attention to the situation that the last number is the target number.

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        if j < 0:
            return [-1, -1]
        left = self.searchLeft(nums, target, i, j)
        if nums[left] != target:
            return [-1, -1]
        right = self.searchLeft(nums, target+1, left, j)
        if nums[right] != target:
            right -= 1
        return [left, right]
        
    
    #search the first number equal to the target
    def searchLeft(self, nums, target, i, j):
        while i < j:
            mid = i + (j-i)/2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        return i
            
