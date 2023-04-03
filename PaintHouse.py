# dp 3xn array
# dp[i][j] = min(dp[i-1][k!=j])
# return the cost
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # create 2d array n x 3 
        dp = [[0]*3 for i in range(len(costs))]

        for i in range(3):
            dp[0][i] = costs[0][i]

        for i in range(1, len(costs)):
            for j in range(3):
                if j==0: 
                    dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + costs[i][j]
                elif j==1: 
                    dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + costs[i][j]
                else: 
                    dp[i][j] = min(dp[i-1][1], dp[i-1][0]) + costs[i][j]

        return min(dp[-1][0], dp[-1][1], dp[-1][2])
