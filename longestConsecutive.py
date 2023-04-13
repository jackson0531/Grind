# given an arr, return the length of the longest sequence 
# no sorting since within O(n); use set to elimnate duplicates and check num+1 exists
# first check if num-1 exists if it does then skip 
# we only want to check every start of a sequence 
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myset = set(nums) # no duplicates
        ans = 0
        for num in myset: 
            if num-1 not in myset: 
                length = 0
                value = num
                while value in myset: 
                    length+=1
                    value+=1
                ans = max(ans, length)

        return ans
