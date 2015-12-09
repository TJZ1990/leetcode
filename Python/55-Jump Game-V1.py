#maxJump means the farthest reachable position.
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxJump = 0
        i = 0
        while maxJump < len(nums)-1 and i <= maxJump:
            maxJump = max(nums[i]+i, maxJump)
            i += 1
        return maxJump >= len(nums)-1
