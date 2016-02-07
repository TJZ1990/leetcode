class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.calIp(s, 0, [], result)
        return result
        
    def calIp(self, s, start, var, result):
        if len(var) > 4:
            return
        elif start == len(s) and len(var) == 4:
            result.append('.'.join(var))
            return
        
        for i in range(start, start+3):
            if i >= len(s):
                break
            if s[start] == '0' and i > start:
                break
            if i == start+2 and s[start:start+3] > '255':
                break
            self.calIp(s, i+1, var+[s[start:i+1]], result)
                    
