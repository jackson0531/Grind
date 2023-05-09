# create a result arr with size of n 
# map: key is index, value is the color 
# when inserting a pair, case 1: originally 0 then check both sides and plus
# case 2: not the same as the original value, then check both sides and minus
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        result = [0]*len(queries)
        myMap = defaultdict(int)
        for index, q in enumerate(queries): 
            if index==0: 
                myMap[q[0]] = q[1]
                continue
            # minus from the reuslt
            if myMap[q[0]]: 
                result[index] -= (myMap[q[0]-1]==myMap[q[0]]) + (myMap[q[0]+1]==myMap[q[0]])
            # add to myMap
            myMap[q[0]] = q[1]
            result[index] += (myMap[q[0]-1]==myMap[q[0]]) + (myMap[q[0]+1]==myMap[q[0]])
            result[index] += result[index-1]

        return result
