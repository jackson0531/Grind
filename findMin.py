# find the not normal side since half is either increasing or not
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]>nums[r]: #left side is sorted
                l = mid+1
            else: #right side is sorted
                r = mid
        return nums[l]
