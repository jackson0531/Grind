# given mxn int matrix, each row and col is sorted 
# return true in target is in the maxtrix, false otherwise
# start with the middle row and 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num, m, n = 0, len(matrix), len(matrix[0])
        while num<m and matrix[num][-1]<target:
            num+=1
        if num == m: 
            return False
        row = matrix[num]
        left, right = 0, n-1
        while left<right: 
            mid = (left+right)//2
            if target<=row[mid]: 
                right = mid
            else: 
                left = mid + 1 

        return row[left]==target  
