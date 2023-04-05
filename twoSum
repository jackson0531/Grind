class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map1 = {}
        for index, num in enumerate(nums):
            if (not((target-num) in map1)):
                map1[num] = index
            else:
                return [map1.get(target-num), index]
