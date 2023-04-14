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
                result.append("".join(temp))
                return
            if (left>0): # allowed (
                temp.append("(")
                backtrack(result, temp, left-1, right)
                temp.pop()
            if (right>left):
                temp.append(")")
                backtrack(result, temp, left, right-1)
                temp.pop()
        backtrack(result, [], n, n)
        return result
