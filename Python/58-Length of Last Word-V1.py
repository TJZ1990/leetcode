class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        start = False
        for c in s[::-1]:
            if c == ' ':
                if start:
                    break
            else:
                if not start:
                    start = True
                length += 1
        return length
