# given an int arr, started at the first index, return if we can jump to the last one
# keep updating the target; if the jump is >= target, update the target to the jumped index
# 2 3 1 1 4
# target = 4
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        for i in range(len(nums)-1, -1, -1): 
            if nums[i]+i >= target: 
                target = i
        return target==0
