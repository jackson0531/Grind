# pattern all but current one -> prefix and sufix
# for loop to build prefix and sufix 
# 1 or 0 = 1, prefill with 0s
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        prefix, sufix = [0]*len(nums), [0]*len(nums)
        prefix[0], sufix[-1] = nums[0], nums[-1]
        for i in range(1, len(nums)): 
            prefix[i] = prefix[i-1]|nums[i-1]
        for i in range(len(nums)-2, -1, -1): 
            sufix[i] = sufix[i+1]|nums[i+1]
        prefix[0], sufix[-1] = 0, 0
        factor = 2**k 
        result = 0
        for i in range(0, len(nums)): 
            curr = nums[i]*factor 
            result = max(result, curr|prefix[i]|sufix[i])
        return result
