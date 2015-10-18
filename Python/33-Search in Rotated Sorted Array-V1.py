#initial version
#use binary search twice
#the first time is to find how many steps the old array need to shift to become the current array
#then we can apply binary search in the old array
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return -1
        
        step = 0 #the step the old array need to take to become the current array
        left = 0
        right = length - 1
        while left < right:
            mid = left + (right-left)/2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid
        if nums[left] < nums[0]:
            step = left
        #print("step: %d" % step)
        
        left = 0
        right = length - 1
        while left <= right:
            mid = left + (right-left)/2
            currentMid = (mid+step) % length
            #print(currentMid, nums[currentMid])
            if nums[currentMid] == target:
                return currentMid
            elif nums[currentMid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
        
