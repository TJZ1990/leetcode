class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        integer = "1"
        for _ in xrange(n-1):
            integer = self.read(integer)
        return integer
    
    def read(self, integer):
        result = ""
        pre = integer[0]
        count = 0
        for cur in integer:
            if cur == pre:
                count += 1
            else:
                result += str(count) + pre
                count = 1
                pre = cur
        result += str(count) + pre
        return result
        
