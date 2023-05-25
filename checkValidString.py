# given a string, return if they are valid paren
# *: either ) or nothing OR (
# pmin: minimum ( we have 
# pmax: maximum ( we have
# traverse the string
class Solution:
    def checkValidString(self, s: str) -> bool:
        pmin, pmax = 0, 0
        for l in s: 
            if l =="(": 
                pmin += 1
                pmax += 1
            elif l == ")": 
                pmin -= 1
                pmax -= 1
            else: # when we have star
                pmin = max(pmin-1, 0)
                pmax += 1
            if pmax<0: 
                return False
            if pmin<0: 
                pmin = 0 # the range is from pmin to pmax, and pmax is still available, so only 0 - pmax are avaible
        return pmin==0
