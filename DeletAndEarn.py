# similar to house robber
# create a hashmap and a set 
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashmap
        freq = Counter(nums)
        # a sorted set
        num_set = sorted(list(set(nums)))

        dp = [0] * (len(num_set)+1)
        dp[0] = 0 
        dp[1] = num_set[0]*freq[num_set[0]]
        for i in range(2, len(num_set)+1):
            if num_set[i-1]==num_set[i-2]+1:
                dp[i] = max(num_set[i-1]*freq[num_set[i-1]] + dp[i-2], dp[i-1])
            else: 
                dp[i] = num_set[i-1]*freq[num_set[i-1]] + dp[i-1]
        
        return dp[-1]
