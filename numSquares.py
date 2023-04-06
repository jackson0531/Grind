# given an int, return the least number of perfect squares that sum to n
# dp[i] means the min number of perfect squares that sum to i 
# traverse from 1 to n and calculate the min
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)

        return dp[-1]
