#version 2
#use binary search to find the left boundary and right boundary
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        left = self.searchLeft(nums, target, i, j)
        if left == -1:
            return [-1, -1]
        right = self.searchRight(nums, target, left, j)
        return [left, right]
        
    
    #search the first number equal to the target
    def searchLeft(self, nums, target, i, j):
        while i < j:
            mid = i + (j-i)/2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if nums[i] == target:
            return i
        else:
            return -1
    
    #search the last number equal to the target
    def searchRight(self, nums, target, i, j):
        while i < j:
            mid = i + (j-i)/2 + 1 #make mid biased to right
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        if nums[i] == target:
            return i
        else:
            return -1
            
            
