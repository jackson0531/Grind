# given a mtrix with pos ints, move to next col
# reqirements: next move > current and return maximum num of moves possible
# also can start anywhere
# pick the smallest num that is bigger than curr
# 2d dp, start wiht the first col

# think about when a spot is not reachable by the first column and it keeps counting
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        result = [[0]*col for i in range(row)]
        ans = 0
        if col==1: 
            return 0
        for j in range(1, col): 
            for i in range(row): 
                a, b, c, curr = 0, 0, 0, grid[i][j]
                if i-1>=0 and grid[i-1][j-1]<curr: 
                    a = 1+result[i-1][j-1]
                if i+1<row and grid[i+1][j-1]<curr: 
                    c = 1+result[i+1][j-1]
                if grid[i][j-1]<curr: 
                    b = 1+result[i][j-1]
                result[i][j] = max(a, b, c)
                ans = max(ans, result[i][j])
                if result[i][j]==0: 
                    grid[i][j] = float('inf')
            if j == 1 and ans == 0: 
                return 0

        return ans
