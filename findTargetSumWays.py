# given a list and a target, return the number of ways to sum to target
# since the order is just one, no backtrack needed, just normal recursion √ 
# TLE recursion; Now, memoization 
# if sum<target, return 0
# As we generate new numbers, we count the number of ways; expand discoveries
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums)<target or target<-1*sum(nums): 
            return 0
        result = collections.defaultdict(int)
        result[0] = 1
        for num in nums: 
            temp = collections.defaultdict(int)
            for t in result: 
                temp[t-num] += result[t]
                temp[t+num] += result[t]
            result = temp
        return result[target]

        # count = defaultdict(int)
        # count[0] = 1
        # for x in nums:
        #     step = defaultdict(int)
        #     for y in count:
        #         step[y + x] += count[y]
        #         step[y - x] += count[y]
        #     count = step

        # return count[target]
