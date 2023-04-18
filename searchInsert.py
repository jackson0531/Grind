# sorted arr, target and return inserted in order
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)
        while l < r:
            mid = (r-l)//2 + l
            if target<=nums[mid]:
                r = mid
            else: 
                l = mid+1
        return l
