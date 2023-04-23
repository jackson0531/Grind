# n piles of bananas, ith pile has piles[i] bananas, return min int k that can eat all piles 
# max is max of bananas and min is 1
# helper class checks if koko can finish 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(speed: int) -> bool: 
            hours = 0 
            for pile in piles:
                hours+=math.ceil(pile/speed)
            return hours<=h
        
        l, r = 1, max(piles)
        while l<r: 
            mid = l+(r-l)//2
            if (helper(mid)): 
                r = mid
            else: 
                l = mid+1
        return l 
