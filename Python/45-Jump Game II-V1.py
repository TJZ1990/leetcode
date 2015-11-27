#initial version
#greedy algorithm, jump to the point with maximum range each time
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        pos = 0
        lastBound = 0
        while pos != len(nums) - 1:
            if pos + nums[pos] >= len(nums) - 1:
                pos = len(nums) - 1
            else:
                maxL = nums[lastBound+1] + lastBound + 1
                nextPos = lastBound + 1
                for i in range(lastBound+2, pos+nums[pos]+1):
                    if nums[i] + i > maxL:
                        maxL = nums[i] + i
                        nextPos = i
                lastBound = maxL
                pos = nextPos
            step += 1
        
        return step
