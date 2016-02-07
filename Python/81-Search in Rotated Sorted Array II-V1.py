# special case: 11311
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            #print left, right
            mid = left + (right-left)/2
            if nums[mid] == target:
                return True
            elif nums[left] < nums[mid]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid -1
            else:
                left += 1
            
        return False
