# given two strings, return true iif s2 contains s1; false otherwise
# s2 is longer
# have arr1 for s1
# window size = len(s1)
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        arr1 = [0]*26
        for ch in s1:
            arr1[ord(ch)-ord('a')]+=1
        l, r = 0, 0
        arr2 = [0]*26
        while r<len(s2):
            arr2[ord(s2[r])-ord('a')]+=1
            while r-l>=len(s1): 
                arr2[ord(s2[l])-ord('a')]-=1
                l+=1
            if (arr1==arr2): 
                return True
            r+=1
        return False
            
