class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        topLeft, bottomRight = [[0]*n for i in range(m)], [[0]*n for i in range(m)]
        for i in range(0, m): 
            j, mySet = 0, set()
            while i<m and j<n: 
                topLeft[i][j] = len(mySet)
                mySet.add(grid[i][j])
                i+=1
                j+=1
        for j in range(0, n): 
            if j == 0: continue
            i, mySet = 0, set()
            while i<m and j<n: 
                topLeft[i][j] = len(mySet)
                mySet.add(grid[i][j])
                i+=1
                j+=1
        for i in range(m-1, -1, -1): 
            j, mySet = n-1, set()
            while i>=0 and j>=0: 
                bottomRight[i][j] = len(mySet)
                mySet.add(grid[i][j])
                i-=1
                j-=1
        for j in range(n-1, -1, -1): 
            if j == n-1: continue
            i, mySet = m-1, set()
            while i>=0 and j>=0: 
                bottomRight[i][j] = len(mySet)
                mySet.add(grid[i][j])
                i-=1
                j-=1
        result = [[0]*n for i in range(m)]
        for i in range(m): 
            for j in range(n): 
                result[i][j] = abs(topLeft[i][j] - bottomRight[i][j])
        return result
