# permutation, trying all possibilities, list contains duplicates
# use a boolean list to check which one is used
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False]*len(nums)
        self.backtrack(nums, result, used, [], 0)
        return result
    def backtrack(self, nums: List[int], result: List[List[int]], used: List[bool], temp: List[int], index: int): 
        if len(temp)==len(nums): 
            result.append(list(temp))
            return
        for i in range(len(nums)): 
            if used[i]: 
                continue
            if i>0 and nums[i]==nums[i-1] and not used[i-1]: 
                continue
            temp.append(nums[i])
            used[i] = True
            self.backtrack(nums, result, used, temp, 0)
            temp.pop()
            used[i] = False
