class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
            
        a = 1
        b = 1
        for i in range(1, len(s)):
            if '1' < s[i-1:i+1] <= '26':
                if s[i] == '0':
                    b, a = a, b
                else:
                    b, a = b+a, b
            elif s[i] == '0':
                return 0
            else:
                b, a = b, b
        return b
                
