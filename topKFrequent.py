# given an arr, return k most freqent elements 
# map num to freq
# Priority q that takes the top k ints
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map1 = {}
        for num in nums: 
            map1[num] = map1.get(num, 0)+1
        return heapq.nlargest(k, map1.keys(), key=map1.get)
