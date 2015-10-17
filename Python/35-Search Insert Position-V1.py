class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #binary search
        low = 0
        high = len(nums)-1

        while low < high:
            mid = low + (high - low)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if target > nums[low]:
            return low + 1
        else:
            return low
