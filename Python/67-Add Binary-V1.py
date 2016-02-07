class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            return self.addBinary(b, a)
        
        b = '0'*(len(a)-len(b)) + b
        
        carry = 0
        result = ''
        for i in reversed(range(len(a))):
            s = int(a[i]) + int(b[i]) + carry
            result = str(s%2) + result
            carry = s / 2
        
        if carry:
            result = '1' + result
        
        return result
        
        
        
        
        
        
        
        
