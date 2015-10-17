#initial version
#the code is ugly

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low)/2
            if nums[mid] == target:
                l = self.searchLow(nums, target, low, mid-1)
                h = self.searchHigh(nums, target, mid+1, high)
                if l == -1:
                    l = mid
                if h == -1:
                    h = mid
                return [l, h]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]
            
    
    def searchHigh(self, nums, target, low, high):
        while low <= high:
            mid = low + (high - low)/2
            if nums[mid] == target:
                result = self.searchHigh(nums, target, mid+1, high)
                if result != -1:
                    return result
                else:
                    return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
                
    def searchLow(self, nums, target, low, high):
        while low <= high:
            mid = low + (high - low)/2
            if nums[mid] == target:
                result = self.searchLow(nums, target, low, mid-1)
                if result != -1:
                    return result
                else:
                    return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
