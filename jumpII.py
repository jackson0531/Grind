# given an arr, starts at nums[0]
# dp[i] the min num of steps takes to get to ith position 
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for index, num in enumerate(nums): 
            # if dp[index] is not equal to i then skip
            for i in range(1, num+1): 
                if index+i<len(nums) and dp[index+i] == 0: 
                    dp[index+i] = dp[index]+1
                    if index+i == len(nums)-1: 
                        return dp[index+i]
        return 0
