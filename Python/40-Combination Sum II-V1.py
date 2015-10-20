#The key problem is how to avoid duplicate combinations.
#For example, candidates is [1, 1, 1].
#In this solution, we set a rule that if a number equals its former number and
#the former number is not chosen. Then this number can't be chosen.
#So we will only try [1] [1,1,1] [1,0,0] [0,0,0].
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.result = []
        self.search(candidates, target, 0, 0, [])
        return self.result
    
    def search(self, candidates, target, begin, total, combo):
        #print(begin, combo)
        if total == target:
            self.result.append(combo)
        else:
            for index in range(begin, len(candidates)):
                if total + candidates[index] > target:
                    break
                if index and candidates[index] == candidates[index-1] and index > begin:
                    continue
                self.search(candidates, target, index+1, total+candidates[index], combo+[candidates[index]])
