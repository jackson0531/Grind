# given arr, replace nums[i] with product of rest nums
# in O(n)
# not min or max prob, no sorting
# prefix is product before and excluding current num 
# sufix is product after and excluding current num
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix, sufix, result = [1]*len(nums), [1]*len(nums), [0]*len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            sufix[i] = sufix[i+1]*nums[i+1]
        for i in range(len(nums)):
            result[i] = prefix[i]*sufix[i]

        return result
