# given undirected graph, find the edge that we can remove and eliminate the cycle
# use union find since union find is to find the cycle in the graph
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # initially the parent is themselves
        parent = [i for i in range(0, len(edges)+1)]
        # the size is all 1's
        size = [1]*(len(edges)+1)
        # find the parent
        def find(num): 
            if parent[num]==num: 
                return num
            return find(parent[num])
        def union(x, y): 
            xParent = find(x)
            yParent = find(y)
            if xParent==yParent: 
                result.append(x)
                result.append(y)
            if size[xParent]>=size[yParent]: 
                parent[yParent] = xParent
                size[xParent] += size[yParent]
            else: 
                parent[xParent] = yParent
                size[yParent] += size[xParent]
        result = []
        for edge in edges: 
            union(edge[0], edge[1])
        return result
