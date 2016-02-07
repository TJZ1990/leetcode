#Newton's method
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r
