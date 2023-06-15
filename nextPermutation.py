# find the first non increasing number and swap with the number barely bigger than that
# inplace = swap
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index1, index2, prev = len(nums)-1, 0, float("-infinity")
        while index1>=0 and nums[index1]>=prev: 
            prev = nums[index1]
            index1-=1
        if index1==-1: 
            return nums.sort()
        index2 = index1+1
        for i in range(index1, len(nums)): 
            if nums[index1]<nums[i]: 
                index2 = i
        nums[index1], nums[index2] = nums[index2], nums[index1]
        index1+=1
        mid = (len(nums)-index1)//2
        nums[index1:len(nums)] = sorted(nums[index1:len(nums)])
