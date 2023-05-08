# given an arr with duplicates, return all possible subsets no duplicates
# try all possible combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtrack(nums, result, [], 0)
        return result

    def backtrack(self, nums: List[int], result: List[List[int]], temp: List[int], index: int): 
        result.append(list(temp))
        for i in range(index, len(nums)): 
            if (i>index and nums[i]==nums[i-1]): continue
            temp.append(nums[i])
            self.backtrack(nums, result, temp, i+1)
            temp.pop()
