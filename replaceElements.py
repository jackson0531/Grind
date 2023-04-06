# given arr, replace the element with the greatest to its right and last one is -1
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maximum, arr[-1] = arr[-1], -1
        for i in range(len(arr)-2, -1, -1):
            maximum, arr[i] = max(maximum, arr[i]), maximum
        return arr
