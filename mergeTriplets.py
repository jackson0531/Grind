# given triplets, operation is to take the max of two numbers 
# given target, return if triplets after operations can be the same 
# violation is to take a number bigger than the target -> only when all numbers <= target
# if we ever have target during operation, we will get it at the end
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [0]*3
        for a,b,c in triplets: 
            if a<=target[0] and b<=target[1] and c<=target[2]: 
                result = [max(a, result[0]), max(b, result[1]), max(c, result[2])]
        return result==target
