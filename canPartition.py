# return true if we can divide an array into two equal subsets
# if sum%2 not = 0, then false
# dp, dp[i] means if we can have a sum of i using all nums
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if (total%2 != 0): 
            return False
        dp = [True]+[False]*(total/2)
        
        for num in nums:
            for i in range(total/2,0,-1):
                if (i>=num and dp[i-num]) or dp[i]:
                    dp[i] = True

        return dp[-1]
