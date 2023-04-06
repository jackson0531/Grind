# either the start with the first or the second 
# create two dp 1d list 

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)==1):
            return nums[0]
        # 0 to len(nums)
        dp1, dp2 = [0]*len(nums), [0]*len(nums)
        dp1[0] = nums[0]
        for i in range(1, len(nums)):
            if i==1: 
                dp1[i] = max(nums[0:2])
                continue
            dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])

        for i in range(1, len(nums)):
            if i==1: 
                dp2[i] = nums[i]
                continue
            dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])
        return max(dp1[-2], dp2[-1])
