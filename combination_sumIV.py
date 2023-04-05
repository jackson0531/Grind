# given an array of unique ins and a target, return how many possible combo that add up to target
# n x target+1
# 1d array
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]*(target+1) #creates an array
        dp[0] = 1
        for total in range(1, target+1):
            for num in nums:
                if total>=num:
                    dp[total] += dp[total-num]
        
        return dp[-1]
