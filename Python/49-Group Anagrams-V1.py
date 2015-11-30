#use a dictionary
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            key = "".join(sorted(str))
            if key in dic:
                dic[key].append(str)
            else:
                dic[key] = [str]
        
        result = []
        for i in dic.values():
            result.append(sorted(i))
            
        return result
