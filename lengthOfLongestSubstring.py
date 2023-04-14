# given a string, find the len of longest substring without repeating chars
# traverse from the beginning, add to a map until we see a duplicate
# when we see a duplicate, move left pointer to map[a]+1
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myMap = {} # char and freq
        l, r = 0, 0
        result = 0
        while r < len(s):
            myMap[s[r]] = myMap.get(s[r], 0) + 1
            while myMap[s[r]]>1:
                myMap[s[l]] -= 1
                l+=1
            result = max(result, r-l+1)
            r+=1
        return result
