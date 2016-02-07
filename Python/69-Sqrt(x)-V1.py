#binary search method
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)/2
            p = mid*mid
            if p <= x and x < (mid+1)*(mid+1):
                return mid
            elif p < x:
                l = mid + 1
            else:
                r = mid
                
