# the net gas after i to i+1 
# two cases: either the first pos index or -1
# total = 0: return -1
# total>0: return the first of total
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if the sum of gas > sum of cost, never 
        if sum(gas)<sum(cost): 
            return -1
        net = [gas[i]-cost[i] for i in range(len(gas))]
        mySum, result = 0, 0
        for index, num in enumerate(net): 
            mySum += num
            if mySum<0: 
                mySum = 0 
                result = index+1
        return result
