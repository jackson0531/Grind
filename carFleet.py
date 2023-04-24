# calculate the time to target
# zip
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(list(zip(position, speed)), key=lambda x:x[0])
        hours = [(target-x[0])/x[1] for x in pair]
        '''
        result, curr = 0, 0
        for hour in hours[::-1]: 
            if hour>curr: 
                result+=1
                curr = hour
        '''
        stack = [] # keeps a decreasing only sequence
        for index, hour in enumerate(hours): 
            while stack and stack[-1]<=hour:
                stack.pop()
            stack.append(hour)
        return len(stack)
