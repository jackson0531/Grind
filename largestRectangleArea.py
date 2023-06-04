# given a list representing historgrams bar height, return the area of largest rectangle in the historgrams
# make a monoctic increasing stack, two pointer technique
# increasing stack because we want to 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append((-1, -1))
        result = 0
        for index, h in enumerate(heights): 
            while stack and stack[-1][0]>=h: 
                p = stack.pop()
                result = max(result, (index-stack[-1][1]-1)*p[0])
            stack.append((h, index))
        while len(stack)>1: 
            p = stack.pop()
            result = max(result, (len(heights)-stack[-1][1]-1)*p[0])
        return result
