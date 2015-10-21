#initial version
#Use a stack to traverse the string.
#If a pair of parentheses is valid, remove them from the stack.
#After that, the stack stores only invalid parenthese.
#Valid parenthese length is the length between two invalid parenthese.
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxL = 0
        for i, c in enumerate(s):
            if c == ')' and stack != [] and stack[-1][1] == '(':
                stack.pop()
            else:
                stack.append((i, c))
        stack.insert(0, (-1, 'x'))
        stack.append((len(s), 'x'))
        
        for i in range(len(stack)):
            if stack[i][0] > stack[i-1][0]:
                maxL = max(maxL, stack[i][0]-stack[i-1][0]-1)

        return maxL
