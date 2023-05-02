# the problem comes down to how do we know when a row or a column is filled
# record each number's position in the matrix 
# for each number in arr, that number row++ and col++
# return if row == m or col == n
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        mapRow, mapCol = {}, {}
        m, n = len(mat), len(mat[0])
        row, col = [0]*len(mat), [0]*len(mat[0])
        for i in range(len(mat)): 
            for j in range(len(mat[0])): 
                mapRow[mat[i][j]] = i
                mapCol[mat[i][j]] = j
        for index, num in enumerate(arr): 
            row[mapRow[num]]+=1
            col[mapCol[num]]+=1
            if row[mapRow[num]]==n or col[mapCol[num]] == m:
                return index
