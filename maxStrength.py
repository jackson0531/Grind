# we can include all pos, but only pairs of negatives
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()
        pos, neg, result, zero = [], [], 1, False
        for num in nums: 
            if num<0: 
                neg.append(num)
            elif num>0: 
                pos.append(num)
            else: 
                zero = True
        if zero and len(pos)==0 and (len(neg)==0 or len(neg)==1): 
            return 0
        if len(pos)==0 and not zero and len(neg)==1: 
            return neg[0]
        if len(neg)%2 == 0: 
            for num in neg: 
                result *= num
        else: 
            for num in range(0, len(neg)-1):
                result *= neg[num]
        for num in pos: 
            result *= num
        return result
