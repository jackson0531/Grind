# do not want to apply to a 
class Solution:
    def smallestString(self, s: str) -> str:
        result = [i for i in s]
        left, right = 0, 0
        while left<len(s) and result[left]=="a": 
            left+=1
        right = left
        if left==len(s): 
            result[-1] = "z"
            return "".join(result)
        while right<len(s) and result[right]!="a": 
            right+=1
        for i in range(left, right): 
            result[i] = chr(ord(result[i])-1)
        return "".join(result)
