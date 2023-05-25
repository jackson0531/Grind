# check for every combo of number
# order is fixed, so no backtrack
# 
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def isRight(index, sq, total): 
            if index==len(sq) and total == 0: 
                return True
            if total<0: 
                return False
            for i in range(index, len(sq)): 
                par = int(sq[index:i+1])
                if isRight(i+1, sq, total-par): 
                    return True
            return False
        result = 0
        for num in range(1, n+1): 
            sq = str(num*num)
            # summ = [int(i) for i in str(sq)]
            if isRight(0, sq, num): 
                result += int(sq)
        return result
