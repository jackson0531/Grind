# given n pairs of (), output all combo
# start with (, (
# backtrack? equal num of (,)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(result, temp, left, right):
            if (left==0 and right==0): 
                result.append(temp)
                return
            if (left>0): # allowed (
                backtrack(result, temp+"(", left-1, right)
            if (right>left):
                backtrack(result, temp+")", left, right-1)
        backtrack(result, "", n, n)
        return result
