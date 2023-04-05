class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        for l in s: 
            dict1[l] = dict1.get(l, 0) + 1
        for l in t:
            dict2[l] = dict2.get(l,0) + 1
        return dict1 == dict2
