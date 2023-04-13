# hashmap to store the values but On in space
# 2. two pointers, while l<r

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l<r:
            s = numbers[l] + numbers[r]
            if (s==target): 
                return [l+1, r+1]
            elif (s<target): 
                l+=1
            else: 
                r-=1
        return [0,0]
