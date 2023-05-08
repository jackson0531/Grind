# given arry, and target, unique combo that sum to target
# sort everything and add to result only if the sum is equal to target
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtrack(candidates, target, result, [], 0)
        return result

    def backtrack(self, candidates: List[int], target: int, result: List[List[int]], temp: List[int], index: int): 
        if target<0: 
            return
        if target==0: 
            result.append(list(temp))
            return
        for i in range(index, len(candidates)): 
            if i>index and candidates[i]==candidates[i-1]: 
                continue
            temp.append(candidates[i])
            self.backtrack(candidates, target-candidates[i], result, temp, i+1)
            
            temp.pop()
