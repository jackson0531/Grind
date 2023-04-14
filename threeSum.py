# retur all triplets that sum equal to 0 
# no duplicates -> set
# hold one number and traverse the next to the end
# O(n^2)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        for index, num in enumerate(nums): 
            target = 0 - num
            l, r = index+1, len(nums)-1
            while (l<r):
                if (nums[l]+nums[r]==target): 
                    result.append((num, nums[l], nums[r]))
                    l+=1
                    r-=1
                elif (nums[l]+nums[r]<target):
                    l+=1
                else: 
                    r-=1

        return list(set(result))
