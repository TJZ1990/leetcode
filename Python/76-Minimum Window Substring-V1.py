# Use a dictionary need to record what and how many words to find in s.
# When found, need[c] += 1. If need[c] < 0, it means we have extra c.
# Use number to record how many valid characters we've got. If number == len(t), we've got all we need.
# Use two pointers i and j, which means the current start and end of the window.
# Make j += 1 in the loop. If number == len(t), move i to get the current minmum window and compare with minL.
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        left = 0
        right = len(s)
        minL = right - left
        i = 0
        number = 0
        for j, c in enumerate(s):
            if c not in need:
                continue
            
            need[c] -= 1
            if need[c] >= 0:
                number += 1
            if number == len(t):
                while s[i] not in need or need[s[i]] < 0:
                    if s[i] in need:
                        need[s[i]] += 1
                    i += 1
                if (j - i) < minL:
                    left, right, minL = i, j, j-i

        return s[left:right+1] if number == len(t)  else ""
                
                
                
