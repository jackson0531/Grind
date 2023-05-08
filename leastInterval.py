# given an array, n as cooldown period when executing same tasks at the same time
# max freq - 1 * n + 1* # of max freq
# what if there are leftovers after: strs with smaller freq can fit in b/w the bigger freq; no extra idel time needed
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0: 
            return len(tasks)
        freq = Counter(tasks)
        maxFreq = 0
        numOfMax = 0
        for key, val in freq.items(): 
            if val>maxFreq: 
                maxFreq = val
                numOfMax = 1
            elif val == maxFreq: 
                numOfMax+=1
        return max((maxFreq-1)*(n+1) + 1*numOfMax, len(tasks))
