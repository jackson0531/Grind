# reuturns the maximum num of fish 
# 0 means no travel, others mean yes
# whenever we see a nonzero num, we dfs; have a boolean value
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        result = 0
        m, n = len(grid), len(grid[0])
        # visit = ([False]*n for i in range(m))
        for i in range(m): 
            for j in range(n): 
                if grid[i][j]!=0: 
                    result = max(result, self.dfs(i, j, grid))
        return result
                
    

    def dfs(self, i: int, j: int, grid: List[List[int]]) -> int:
        # base case
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0: 
            return 0
        total = grid[i][j] 
        grid[i][j] = 0
        total += self.dfs(i-1, j, grid) + self.dfs(i+1, j, grid) + self.dfs(i, j-1, grid) + self.dfs(i, j+1, grid)
        return total
