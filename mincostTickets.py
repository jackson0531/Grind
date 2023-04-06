# three options, 1d arr, if n>day check min of three options 
# dp.i means the min costs to travel by the end of day i
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        map1 = {1:costs[0], 7:costs[1], 30:costs[2]}
        dp = [float('inf')]*(days[-1]+1)
        dp[0] = 0
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i-1]
            else: 
                for j in map1.keys():
                        dp[i] = min(dp[i], dp[max(0, i-j)]+map1[j])

        return dp[-1]
