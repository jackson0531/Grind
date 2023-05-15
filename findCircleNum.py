# given n cities, matrix nxn matrix
# union find: to find the number of connected components
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(0,len(isConnected))]
        size = [1]*len(isConnected)
        def find(x): 
            if parent[x]==x: 
                return x
            return find(parent[x])
        def union(x, y): 
            xParent = find(x)
            yParent = find(y)
            if xParent==yParent: 
                return 0
            if size[xParent]>=size[yParent]: 
                parent[yParent] = xParent
                size[xParent] += size[yParent]
            else: 
                parent[xParent] = yParent
                size[yParent] += size[xParent]
            return 1
        result = len(isConnected)
        for i in range(len(isConnected)): 
            for j in range(len(isConnected)): 
                if isConnected[i][j] == 1: 
                    result -= union(i, j)
        return result
