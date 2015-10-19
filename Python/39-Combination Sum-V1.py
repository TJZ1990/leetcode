#initial version
#recursive method
#sort the array first
#We can repeat one number unlimited number of times.
#But if the current sum adds the current number is bigger than target,
#there's no need to try the latter numbers.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(set(candidates))
        self.result = []
        self.search(candidates, target, 0, 0, [])
        return self.result
    
    def search(self, candidates, target, index, total, combo):
        #print(combo)
        while index < len(candidates) and (total+candidates[index]) <= target:
            self.search(candidates, target, index+1, total, combo)
            total += candidates[index]
            combo = combo + [candidates[index]]
            if total == target:
                self.result.append(combo)
                return
