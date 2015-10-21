#version 2
#improve initial version by calculating maxL dynamically
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxL = 0
        for i in range(len(s)):
            if s[i] == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
                if stack:
                    maxL = max(maxL, i-stack[-1])
                else:
                    maxL = max(maxL, i+1)
            else:
                stack.append(i)
        return maxL
                        
