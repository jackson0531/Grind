# given an arr, return an array such that answer i is the number of days to get a higher num
# no sorting 
# have a stack that only for decreasing number 
# for each num in temps: while stack.peek is < than current num: pop and update the count
# add the tuple num and index into the stack/deque
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = deque()
        result = [0]*len(temperatures)
        for index, num in enumerate(temperatures): 
            while stack and stack[-1][0]<num: 
                result[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
            stack.append((num, index))
        return result
